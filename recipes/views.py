from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect ,get_object_or_404
from todo.models import TodoModel
from todo.forms import TodoForm
from django.views import generic
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Recipe, Ingredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'description']
    template_name = 'recipes/recipe_form.html'
    success_url = reverse('recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse('recipe_list')

class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['name', 'quantity', 'unit', 'recipe']
    template_name = 'recipes/ingredient_form.html'






# class RecipeList(ListView):
# #     recipes = Recipe.objects.all()
# #     return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


# # def recipe_detail(request, recipe_id):
# #     recipe = get_object_or_404(Recipe, id=recipe_id)
# #     ingredients = recipe.ingredients.all() 
# #     return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})


# # def recipe_create(request):
# #     if request.method == "POST":
# #         form = RecipeForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('recipe_list')
# #     else:
# #         form = RecipeForm()
# #     return render(request, 'recipes/recipe_form.html', {'form': form})


# # def ingredient_create(request):
# #     if request.method == "POST":
# #         form = IngredientForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('recipe_list')
# #     else:
# #         form = IngredientForm()
# #     return render(request, 'recipes/ingredient_form.html', {'form': form})


# # def recipe_delete(request, recipe_id):
# #     recipe = 

