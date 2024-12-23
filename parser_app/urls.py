from django.urls import path
from . import views

urlpatterns = [
    path('jutsu_film_list/', views.JutsuListView.as_view(), name='jutsu_list'),
    path('form_parser_jutsu/', views.JutsuFormView.as_view(), name='form_parser_jutsu'),
]
