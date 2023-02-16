from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('CLIENT', 'Client'),
        ('SERVICE_COMPANY', 'Service_company'),
        ('MANAGER', 'Manager'),
    )

    name = models.CharField(max_length=250)
    description = models.TextField(max_length=600)
    role = models.CharField(choices=ROLE_CHOICES,
                            blank=True, null=True, max_length=20)

    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name
