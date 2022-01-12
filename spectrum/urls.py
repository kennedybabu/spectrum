from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('interest/<int:pk>/', views.interest, name='interest' ),
    path('create_interest/', views.createInterest, name='create_interest'),

]