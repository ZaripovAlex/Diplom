from django.contrib import admin


from django.contrib import admin
from recipe.models import Category, Recipe



# @admin.register(Category)
class RecipeCategoriesAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    search_help_text = "Поиск по полю title"

    fieldsets = [
        (
            'Название',
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Все рецепты в данной категории',
            {
                'classes': ['wide'],
                'fields': ['recipes'],
            },
        ),
    ]


# @admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ["title", "cook_time", "author", "about_image"]
    ordering = ["author"]
    list_filter = ["title", "author"]
    search_fields = ["title"]
    search_help_text = "Поиск по полю title"
    actions = ["delete_title", "delete_description",
               "delete_cooking_steps", "delete_products",
               "delete_image"]

    fieldsets = [
        (
            'Название',
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Описание',
            {
                'classes': ['wide'],
                'fields': ['description'],
            },
        ),
        (
            'Шаги приготовления',
            {
                'classes': ['wide'],
                'fields': ['cooking_steps'],
            },
        ),
        (
            'Продукты',
            {
                'classes': ['wide'],
                'fields': ['products'],
            },
        ),
        (
            'Время приготовления',
            {
                'classes': ['wide'],
                'fields': ['cook_time'],
            },
        ),
        (
            'Картинка для рецепта',
            {
                'classes': ['wide'],
                'fields': ['image'],
            },
        ),
        (
            'Автор рецепта',
            {
                'classes': ['wide'],
                'fields': ['author'],
            },
        ),
    ]

    @admin.action(description="Удалить название")
    def delete_title(self, request, queryset):
        queryset.update(title="")

    @admin.action(description="Удалить описание")
    def delete_description(self, request, queryset):
        queryset.update(description="")

    @admin.action(description="Удалить рецепт")
    def delete_cooking_steps(self, request, queryset):
        queryset.update(cooking_steps="")

    @admin.action(description="Удалить продукты")
    def delete_products(self, request, queryset):
        queryset.update(products="")

    @admin.action(description="Удалить картинку")
    def delete_image(self, request, queryset):
        queryset.update(image="")

    def about_image(self, obj):
        if obj.image:
            return 'YES picture'
        else:
            return 'NO picture'
