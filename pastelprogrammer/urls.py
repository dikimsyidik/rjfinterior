"""pastelprogrammer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from basic_app.views import index,contact,gallery,tentang_kami
from admin_rjf.views import logout_views,login
from django.contrib.auth import views as auth_views



urlpatterns = [
  	path('', index,name='home'),
    path('adm/', admin.site.urls),
    path('logout/', logout_views,name='logout'),
    path('tentang_kami/',tentang_kami,name='tentang_kami'),
    path('gallery/',gallery,name='gallery'),
    path('contact/',contact,name='contact'),
    # path('login/',login,name='login'),
    
    path('dashboard/', include('admin_rjf.urls')),

    path('login/', auth_views.LoginView.as_view(template_name="admin_rjf/login_view.html"), name='login'),

]
