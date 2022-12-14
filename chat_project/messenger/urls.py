"""messenger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from chat_auth import views as chat_auth_views

urlpatterns = [
    path('', chat_auth_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('chat/', include('chat_api.urls')),
    path('message/', include('chat_message_api.urls')),
    path('user/', include('chat_user.urls')),
    path('login/', chat_auth_views.login, name='login'),
    path('logout/', chat_auth_views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('user_auth_success/', chat_auth_views.user_auth_success),
    path('check_user_auth/', chat_auth_views.user_auth),
]
