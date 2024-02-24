from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/profiles')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return (f'User:{self.username},'
                f'first_name:{self.first_name}'
                f'last_name:{self.last_name}'
                f'email:{self.email}')
    class Meta:
        verbose_name = 'Параметры пользователя'
        verbose_name_plural ='Пользователи'

    def get_absolute_url(self):
        return reverse('Recipe',kwargs={'id': self.id, 'username': self.username})