from django import forms
from .models import Recipe, Category

class CreteRecipe(forms.Form):
    category = forms.ChoiceField(required=True, label='Категория рецепта',
                                 widget=forms.ChoiceField(choices=Category.objects.all(),))
    title = forms.CharField(required=True, max_length=50, label='Название рецепта')
    description = forms.CharField(required=True, max_length=1000, label='Описание рецепта',
                                  widget=forms.Textarea())
    cooking_stages = forms.CharField(required=True, max_length=1000, label='Этапы приготовления')
    ingridients = forms.CharField(required=True, max_length=500, label='Необходимые продукты',
                                  widget=forms.Textarea())
    cook_times = forms.IntegerField(required=True, label='Время приготовления в мин.',widget=forms.IntegerField())
    image = forms.ImageField(required=True, label='Фото готового блюда', widget=forms.ImageField())



class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', widget=forms.CharField())
