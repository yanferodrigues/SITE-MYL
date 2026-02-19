from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('',include('finance.urls')),
    path('',include('gym.urls')), 
    path('', include('about.urls')),
    path('', include('tasks.urls')),
    path('', include('user.urls')),
]
