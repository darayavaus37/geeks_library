from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  
    path('recipe/add/', views.recipe_create, name='recipe_add'),  
    path('ingredient/add/', views.ingredient_create, name='ingredient_add'), 
    path('recipe/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),  
]
