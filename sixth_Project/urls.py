"""
URL configuration for sixth_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from .import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('',views.HOME,name='home'),
    path('about/',views.ABOUT,name="about"),

    path('product/<slug:slug>',views.PRODUCT_DETAIL,name="product_detail"),
    path('product',views.PRODUCT,name="product"),
    # path('product/filter-data',views.filter_data,name="filter_data"),
    path('product/filter-data',views.filter_data,name="filter-data"),


    path('404',views.ERROR,name='error'),
    path('account/my_account',views.MY_ACCOUNT,name='my_account'),
    path('account/register',views.REGISTER,name='handleregister'),
    path('account/login',views.LOGIN,name='handlelogin'),
    path('account/profile',views.PROFILE,name='profile'),
    path('account/profile/update',views.PROFILE_UPDATE,name="profile_update"),
    path('accounts/',include('django.contrib.auth.urls'))

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
