from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('stats/', include('stats.urls')),
]
