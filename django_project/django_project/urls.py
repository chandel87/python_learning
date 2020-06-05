"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views   #other  way of adding urls, don't need to add users/urls.py in this  case
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('blog/', include('blog.urls')),
    path('', include('blog.urls')),   # this makes blog app as our global home page, can access  things of it without prefixing with "blog/"

    # path('register/', include('users.urls')),
    path('register/', user_views.register, name="register"),


    # using inbuilt login/logout views
    # also, by default python looks for templates of login/logout in "registration/login.html" directory
    # so we can either define our templates either in default "registration" folder or we can
    # define our own directory for python to look for, and  we do that by using "template_name" in as_view()

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout")

]
