from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Vegetable, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        user = User(name=name, phone=phone, address=address)
        user.set_password(password)
        user.save()

        return redirect('login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard' if user.is_superuser else 'dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid phone or password'
            })

    return render(request, 'login.html')




def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def vegetable_list(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'vegetables.html', {'vegetables': vegetables})

@login_required
def add_to_cart(request, veg_id):
    veg = Vegetable.objects.get(id=veg_id)
    qty = int(request.POST['quantity'])

    if qty > veg.quantity_available:
        messages.error(request, f"Only {veg.quantity_available} kg available for {veg.name}")
        return redirect('vegetables')

    total = veg.price_per_kg * qty
    CartItem.objects.create(user=request.user, vegetable=veg, quantity=qty, total_price=total)
    
    messages.success(request, f"{qty} kg of {veg.name} added to cart! 🛒")
    return redirect('dashboard')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart')

    order = Order.objects.create(user=request.user)
    for item in cart_items:
        # ✅ Reduce stock
        veg = item.vegetable
        if item.quantity <= veg.quantity_available:
            veg.quantity_available -= item.quantity
            veg.save()

        # ✅ Save order item
        OrderItem.objects.create(
            order=order,
            vegetable=veg,
            quantity=item.quantity,
            total_price=item.total_price
        )
    cart_items.delete()
    return render(request, 'order_success.html', {'order': order})

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    return render(request, 'order_history.html', {'orders': orders})


@login_required
def dashboard(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'dashboard.html', {'vegetables': vegetables})

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    vegetables = Vegetable.objects.all()
    orders = Order.objects.all().order_by('-ordered_at')
    return render(request, 'admin_dashboard.html', {
        'vegetables': vegetables,
        'orders': orders,
    })
@login_required
def update_stock(request, veg_id):
    if request.method == 'POST' and request.user.is_superuser:
        veg = Vegetable.objects.get(id=veg_id)
        add_qty = int(request.POST.get('new_quantity', 0))
        veg.quantity_available += add_qty
        veg.save()
    return redirect('admin_dashboard')
@login_required
def delete_order(request, order_id):
    if request.user.is_superuser:
        order = Order.objects.get(id=order_id)
        order.delete()
    return redirect('admin_dashboard')
@login_required
def remove_cart_item(request, item_id):
    item = CartItem.objects.get(id=item_id, user=request.user)
    item.delete()
    return redirect('cart')
