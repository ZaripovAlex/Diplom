from django.db import models

from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категории рецептов'
        verbose_name_plural = 'Категории рецептов'

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    cooking_stage = models.TextField()
    ingredients = models.TextField(blank=True)
    cook_time = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Recipe:{self.title}'
                f'description:{self.description}'
                f'ingredients:{self.ingredients}'
                f'cooking_stage:{self.cooking_stage}'
                f'cook_time:{self.cook_time}'
                f'author:{self.author}')
    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'Рецепты'

