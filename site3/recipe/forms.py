from django import forms
from django.shortcuts import get_object_or_404
from .models import Recipe, Category


# class CreteRecipe(forms.Form):
    # # choice = get_object_or_404(Category)
    # # category = forms.ChoiceField(required=True, label='Категория рецепта',
    # #                              widget=forms.Select(choices=Category.objects.get().all(),))
    # title = forms.CharField(required=True, max_length=50, label='Название рецепта')
    # description = forms.CharField(required=True, max_length=1000, label='Описание рецепта',
    #                               widget=forms.Textarea())
    # cooking_stages = forms.CharField(required=True, max_length=1000, label='Этапы приготовления')
    # ingridients = forms.CharField(required=True, max_length=500, label='Необходимые продукты',
    #                               widget=forms.Textarea())
    # cook_times = forms.IntegerField(required=True, label='Время приготовления в мин.', widget=forms.IntegerField())
    # image = forms.ImageField(required=True, label='Фото готового блюда', widget=forms.ImageField())

class CreteRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('category', 'title', 'description', 'cooking_stage', 'ingredients', 'cook_time','author')
        classes =[]


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', widget=forms.CharField())
