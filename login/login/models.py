from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class MyUser(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=60, unique=True)
    email = models.EmailField(verbose_name='email', max_length=240, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.username
