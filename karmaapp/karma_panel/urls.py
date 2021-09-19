"""karmaapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from karmaapp import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('forgot_pwd',views.forgot_pwd, name='forgot_pwd'),
    path('reset_page',views.reset_page, name='reset_page'),
    path('reset_pwd',views.reset_pwd, name='reset_pwd'),
    path('register',views.register, name='register'),
    path('logout',views.logout,name="logout"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('addproduct',views.addproduct,name="addproduct"),
    #path('category',views.category,name="category"),
    path('category',views.category,name="category"),
    path('add_to_cart/<int:pk>',views.add_to_cart,name="add_to_cart"),
    path('cart',views.CartPage,name="cart"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    