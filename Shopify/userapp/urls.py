from django.urls import path
from userapp.views import UserRegisterView
from django.contrib.auth import views as  auth_views

urlpatterns = [
    path('register/<str:role>/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

 