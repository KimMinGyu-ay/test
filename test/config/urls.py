from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from main import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("main.urls")),    
    path("main/",views.home)
]
