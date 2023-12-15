from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('profile/', views.profilepage, name='profile'),
    path('register/', views.registerpage, name='register'),
    path('login_firebase/', views.login_firebase, name='login_firebase'),
    path('register_auth/', views.register_auth, name='register_auth'),
]
