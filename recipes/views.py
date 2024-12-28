from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.all() 
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


def ingredient_create(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = IngredientForm()
    return render(request, 'recipes/ingredient_form.html', {'form': form})


def recipe_delete(request, recipe_id):
    recipe = 

