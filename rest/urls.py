from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest.app.user.urls')),
    path('api/', include('rest.app.profile.urls')),
]
