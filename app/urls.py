from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('vegetables/', views.vegetable_list, name='vegetables'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:veg_id>/', views.add_to_cart, name='add_to_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('orders/', views.order_history, name='order_history'),
    path('dashboard/', views.dashboard, name='dashboard'),
path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
path('update-stock/<int:veg_id>/', views.update_stock, name='update_stock'),
path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
path('remove-cart-item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),


]
