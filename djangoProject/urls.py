"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib import admin
from django.urls import path ,include
from todo import views


urlpatterns = [
    path('', views.landingpage, name="landing-page"),

    path('index/', views.index, name="todo"),
    path('register/', views.register, name="register"),  # Register page URL
    path('main/', views.main, name="main"),
    path('login/', views.user_login, name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),

]
