from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('interest/<int:pk>/', views.interest, name='interest' ),
    path('create_interest/', views.createInterest, name='create_interest'),
    path('update_interest/<int:pk>/', views.updateInterest, name='update_interest'),
    path('delete_interest/<int:pk>/', views.deleteInterest, name='delete_interest'),
    path('profile/<int:pk>/', views.userProfile, name='user_profile'),
]