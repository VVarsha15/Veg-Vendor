from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone




class UserManager(BaseUserManager):
    def create_user(self, phone, name, address, password=None):
        if not phone:
            raise ValueError('Users must have a phone number')
        user = self.model(phone=phone, name=name, address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name, address, password=None):
        user = self.create_user(phone, name, address, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):  # 👈 include PermissionsMixin
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField()

    is_staff = models.BooleanField(default=False)       # 👈 required for admin
    is_superuser = models.BooleanField(default=False)   # 👈 already used
    is_active = models.BooleanField(default=True)       # 👈 also commonly used

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'address']

    objects = UserManager()

    def __str__(self):
        return self.name


# Vegetable listing
class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    price_per_kg = models.FloatField()
    quantity_available = models.IntegerField(default=0)
    image_filename = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Cart item
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}kg of {self.vegetable.name} by {self.user.name}"
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(default=timezone.now)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()