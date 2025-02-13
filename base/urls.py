from django.urls import path
from . import views

urlpatterns = [
      path('', views.login_user , name= 'login' ),
   path('home/', views.home_view ,name= 'home'),
   path('members/',views.members_view, name='member'),
   path('deposits/',views.deposits_view, name='deposit'),
   path('deposit_history/',views.deposit_history,name='history'),
  
    
]