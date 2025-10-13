from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.game_create, name='game_create'),
    path('update/<int:pk>/', views.game_update, name='game_update'),
    path('delete/<int:pk>/', views.game_delete, name='game_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('like/<int:pk>/', views.game_like, name='game_like'),
    path('dislike/<int:pk>/', views.game_dislike, name='game_dislike'),
]
