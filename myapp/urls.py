from django.contrib import admin
from django.urls import path, include  # include is used to include other URL configs

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin site
    path('', include('your_app.urls')),  # Include app-specific URLs
]