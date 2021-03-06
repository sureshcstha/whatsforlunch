"""mysite URL Configuration

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
from django.urls import path
from lunch import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('restaurants/', views.restaurant_list, name="restaurant_list"),
    path('restaurants/<int:restaurant_id>', views.detail, name="detail"),
    path('add/', views.add_restaurant, name="add_restaurant"),
    path('update/<int:id>', views.update_restaurant, name="update_restaurant"),
    path('delete/<int:id>', views.delete_restaurant, name="delete_restaurant"),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
