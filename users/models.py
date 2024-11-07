from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True,
                                    help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар')
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

