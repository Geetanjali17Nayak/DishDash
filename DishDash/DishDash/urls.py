"""
URL configuration for DishDash project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import *


urlpatterns = [
    path('recipes/' , recipe , name="recipes"),
    path('update_recipe/<int:id>/' , update_recipe , name="update_recipes"),
    path('delete_recipe/<int:id>/' , delete_recipe , name="delete_recipe"),
    path('admin/', admin.site.urls),
    path('login_page/' , login_page , name="login_page"),
    path('register/' , register , name="register"),
    path('logout_page/' , logout_page , name="logout_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=staticfiles_urlpatterns()    
