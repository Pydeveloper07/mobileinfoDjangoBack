from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('like/', views.like, name='like'),
    path('comment/', views.add_comment, name="comment"),
    path('like_comment/', views.like_comment, name="like_comment"),
    path('search/', views.search, name='search'),
]