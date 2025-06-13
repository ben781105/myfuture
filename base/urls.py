from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.login_user , name= 'login' ),
   path('', views.home_view ,name= 'home'),
   path('members/',views.members_view, name='member'),
   path('deposits/',views.deposits_view, name='deposit'),
   path('deposit_history/',views.deposit_history,name='history'),
  
    
]