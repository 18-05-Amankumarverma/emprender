from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('users/',views.users,name='users'),
    path('addusers/',views.add_users,name='add_users')
]