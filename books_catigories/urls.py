from django.urls import path
from . import views
urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('child_books/', views.child_books, name='child_books'),
    path('elderly_books/', views.elderly_books, name='elderly_books'),
    path('teen_books/', views.teen_books, name='teen_books'),
    path('youth_books/', views.youth_books, name='youth_books'),
]