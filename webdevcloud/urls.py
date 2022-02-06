from django.contrib import admin
from django.urls import path

from . import views
from stats import views as statVies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('stats/', statVies.index),
]
