from django.contrib.auth.backends import ModelBackend
from .models import User

class PhoneBackend(ModelBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        print("📞 Authenticating phone:", phone)

        try:
            user = User.objects.get(phone=phone)
            print("👤 Found user:", user.name)
            if user.check_password(password):
                print("✅ Password match!")
                return user
            else:
                print("❌ Password mismatch")
        except User.DoesNotExist:
            print("❌ No user with this phone")

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
