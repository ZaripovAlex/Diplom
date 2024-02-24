from django.urls import path

from recipe import views

from recipe.views import CreateRecipe

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('recipe/<int:recipe_id>', views.recipe, name='Recipe'),
    path('category/<int:category_id>', views.recipes_by_category, name='Recipe by category'),
    path('search/<str:query>', views.search_recipes, name='Search recipes'),
    # path('add/', views.create_recipe, name='Create recipe'),
    path ('add/', CreateRecipe.as_view(), name='Create recipe'),
]