
from django.contrib import admin
from .models import User
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email",
                    "is_active", "is_staff", "is_superuser", "date_joined", "last_login"]
    search_fields = ["email", "first_name", "last_name"]
    search_help_text = "Поиск по полям email, first_name, last_name."

    fieldsets = [
        (
            'Пароль',
            {
                'description': 'хэш пароля пользователя',
                'classes': ['collapse'],
                'fields': ['password'],
            },
        ),
        (
            'Дата регистрации',
            {
                'description': 'Дата регистрации пользователя',
                'classes': ['collapse'],
                'fields': ['date_joined'],
            },
        ),
        (
            'Дата последнего входа',
            {
                'description': 'Дата последнего входа пользователя',
                'classes': ['collapse'],
                'fields': ['last_login'],
            },
        ),
        (
            'Статус активации учетной записи',
            {
                'description': 'Статус активации учетной записи пользователя',
                'classes': ['wide'],
                'fields': ['is_active'],
            },
        ),
        (
              'Статус песонала',
            {
                'description': 'Является пользователь персоналом',
                'classes': ['wide'],
                'fields': ['is_staff'],
            },
         ),
        (
            'Статус суперпользователя',
            {
                'description': 'Является пользователь суперпользователем',
                'classes': ['wide'],
                'fields': ['is_superuser'],
            },
        ),
        (
            'Права пользователя',
            {
                'description': 'Какими правами наделен пользователь',
                'classes': ['wide'],
                'fields': ['user_permissions'],
            },
        ),
        (
            'Группы пользователя',
            {
                'description': 'Группы в которых состоит пользователь',
                'classes': ['wide'],
                'fields': ['groups'],
            },
        ),
        (
            'Логин пользователя',
            {
                'description': 'Логин пользователя - бесполезен почти не за что не отвечает',
                'classes': ['wide'],
                'fields': ['username'],
            },
        ),
        (
            'Имя пользователя',
            {
                'description': 'Имя пользователя - не обязательное поле',
                'classes': ['wide'],
                'fields': ['first_name'],
            },
        ),
        (
            'Фамилия пользователя',
            {
                'description': 'Фамилия пользователя - не обязательное поле',
                'classes': ['wide'],
                'fields': ['last_name'],
            },
        ),
        (
            'Электронная почта пользователя',
            {
                'description': 'Подвержденная электронная почта пользователя (очень важное поле)',
                'classes': ['wide'],
                'fields': ['email'],
            },
        ),



    ]

    @admin.action(description="Деактивировать аккаунт")
    def deactivate_accounts(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description="Активировать аккаунт")
    def activate_accounts(self, request, queryset):
        queryset.update(is_active=True)