from django.urls import path
from . import views

urlpatterns = [
      path('api/v1/listUsers',views.listUsers,name='listUsers'), # get list no. of users
      path('api/v1/createAccount',views.createAccount,name='createAccount'), 
      path('api/v1/login',views.loginUser,name='loginUser')
]