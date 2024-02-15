import random

from django.shortcuts import render, get_object_or_404

from site3.recipe.models import Recipe, Category


def home(request):

    recipes = Recipe.objects.all()
    if len(recipes)<5:
        recipes_list = [recipes]
    else:
        recipes_list = [random.sample(recipes,5)]

    context = {
        'title': "Главная страница",
        'recipe': recipes_list
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html',{'title': 'О нас'})

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'title': f'Рецепт: {recipe.title}',
        'recipe': recipe
    }
    return render(request, 'recipe.html', context)

def recipes_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'title': f'Рецепты по категории: {category}',
        'recipes': get_object_or_404(Recipe, category=category)
    }
    return render(request, 'recipes_list.html', context)

def search_recipes(request, query:str):
    if query:
        recipes = Recipe.objects.filter(title__icontains=query).order_by('title')
    context = {
        'title': 'Поиск рецепта',
        'recipes': recipes
    }
    return render(request, 'recipes_search.html', context)




