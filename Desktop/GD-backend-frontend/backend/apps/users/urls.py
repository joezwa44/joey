from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.UserSignIn.as_view(), name='user_sign_in'),
    path('singup/', views.UserSignUp.as_view(), name= 'user_sign_up'),
    path('profile/', views.UserProfile.as_view(), name='user_profile'),
]
