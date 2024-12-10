from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/',views.about_view, name='about_view'),
    path('emoji/',views.emoji_view, name='emoji_view'),
    path('photo/',views.image_library_view, name='image_library_view'),
    path('aboutmypets/',views.aboutmypets_view, name='aboutmypets_view'),
    path('time/',views.time_view, name='time_view'),

]