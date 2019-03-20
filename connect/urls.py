from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('/profile', views.userProfile, name='userProfile'),
    path('/profile/<int:id>', views.profile, name='profile'),
    path('/', views.home, name='home')
]
