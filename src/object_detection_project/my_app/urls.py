from django.urls import path
from . import views


urlpatterns = [
    path('', views.login,name='myapp-login'),
    path('home/', views.home,name='myapp-home'),
    path('register/', views.register,name='myapp-home'),

]