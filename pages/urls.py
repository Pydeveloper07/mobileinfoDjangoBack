from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', include('listings.urls')),
    path('send_mail/', views.send_email, name='send_mail'),
]