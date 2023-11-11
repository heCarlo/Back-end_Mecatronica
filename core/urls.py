from django.contrib import admin
from django.urls import path, include
from app.urls import urlpatterns as myapp_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(myapp_urls)),
]
