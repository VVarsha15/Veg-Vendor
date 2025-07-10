from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # 👈 Include your app's URLs
]+ static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'veggiecart/vegetable_static'))
