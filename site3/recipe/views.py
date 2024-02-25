import random

from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .forms import CreteRecipe, SearchForm
from .models import Recipe, Category
from .models import User


def home(request):
    recipe_list=[]
    recipes = Recipe.objects.all()
    if len(recipes) < 5:
        recipe_list.append(recipes)
    else:
         while len(recipe_list)<5:
            recipe_list.append(random.choice(recipes))

    context = {
        'title': "Главная страница",
        'recipe': recipe_list,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'О нас'})

# def create_recipe(request):
#     form = CreteRecipe(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             cooking_stage = form.cleaned_data['cooking_stage']
#             ingredients = form.cleaned_data['ingredients']
#             cook_time = form.cleaned_data['cook_time']
#             category = Category.objects.get(category=request.category.title)
#             author = User.objects.get(username=request.user.username)
#             recipe = Recipe(
#                 title=title,
#                 description=description,
#                 cooking_stage=cooking_stage,
#                 ingredients=ingredients,
#                 cook_time=cook_time,
#                 author=author,
#                 category=category
#             )
#             recipe.save()
#     context = {
#             'title': 'Добавление рецепта',
#             'form': form,
#     }
#     return render(request, 'create_recipe.html', context)

class CreateRecipe(CreateView):
    model = Recipe
    form_class = CreteRecipe
    template_name = 'create_recipe.html'


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
        'recipe': Recipe.objects.filter(category=category).all()
    }
    return render(request, 'recipes_list.html', context)


def category(request, category):
    category = get_object_or_404(Category)
    return render(request, 'category.html', {'category': category})

def search_recipes(request):
    query = request.POST.get('query')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query).order_by('title')
    context = {
        'title': 'Поиск рецепта',
        'recipes': recipes
    }
    return render(request, 'recipes_search.html', context)
