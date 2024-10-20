from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.home_page, name='home'),

    path('search-for-room/', views.search_for_room, name='search_for_room'),
    path('<slug:slug>/', views.hotel_detail_page, name='hotel_detail'),
    path('book-a-room/<slug:slug>/', views.book_a_room, name='book_a_room'),
]

