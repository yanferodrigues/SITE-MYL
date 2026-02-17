from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DASHBOARD.urls')),
    path('',include('FINANCE.urls')),
    path('',include('GYM.urls')), 
    path('', include('ABOUT.urls')),
    path('', include('TASKS.urls')),
    path('', include('USER.urls')),
]
