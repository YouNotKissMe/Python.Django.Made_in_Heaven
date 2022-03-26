from django.urls import path
from .views import profile, RegistrationView
from django.contrib.auth import views


urlpatterns = [
    path('', profile, name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registrations/', RegistrationView.as_view(), name='reg')

]

