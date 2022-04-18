from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name ="user"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('mypage/<int:id>', views.mypage, name='mypage'),
    path('update/<int:id>', views.user_update, name='update'),
    path('update/<int:id>/delete', views.delete, name='delete'),
   
]
