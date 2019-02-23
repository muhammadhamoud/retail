from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.listings,name='listings'),
    path('<int:listing_id>', views.listing_view,name='listing_view'),
    path('search', views.search,name='search'),
]