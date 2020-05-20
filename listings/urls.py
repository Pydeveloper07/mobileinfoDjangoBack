from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('like/', views.like, name='like'),
    path('comment/', views.add_comment, name="comment"),
]