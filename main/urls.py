from . import views
from django.urls import path

urlpatterns = [
    path('course/<str:pk>', views.classBoard, name='course'),
    path('add/', views.addBoard, name='add'),
    path('update-user', views.userBoard, name='update-user'),
    path('sign-in/', views.loginPage, name='sign-in'),
    path('sign-up/', views.registerPage, name='sign-up'),
    path('logout/', views.logoutUser, name='logout'),
    path('success/', views.success, name='success'),
    path('', views.homeBoard, name='home'),
]


