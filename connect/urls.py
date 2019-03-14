from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('login/', views.login, name='login'),#If it recognises path.login it goes to login view, the same applies to signup
    path('signup/', views.signup, name='signup')
    
]