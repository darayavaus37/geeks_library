from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='books'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('aboutme/',views.about_view, name='about_view'),
    path('emoji/',views.emoji_view, name='emoji_view'),
    path('photo/',views.image_library_view, name='image_library_view'),
    path('aboutmypets/',views.aboutmypets_view, name='aboutmypets_view'),
    path('time/',views.time_view, name='time_view'),
    path('contact/', views.contact_view, name='contact_view'),

]