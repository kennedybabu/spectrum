from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('interest/<int:pk>/', views.interest, name='interest' ),
    path('create_interest/', views.createInterest, name='create_interest'),
    path('update_interest/<int:pk>/', views.updateInterest, name='update_interest'),
    path('delete_interest/<int:pk>/', views.deleteInterest, name='delete_interest'),
    path('profile/<int:pk>/', views.userProfile, name='user_profile'),
    path('join_interest/<int:pk>/', views.joinInterest, name='join_interest'),
    path('quit_interest/<int:pk>/', views.quitInterest, name='quit_interest'),
    path('delete_postt/<int:pk>/', views.deletePost, name='delete_post'),



]