from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registration/', views.register, name="register"),
]