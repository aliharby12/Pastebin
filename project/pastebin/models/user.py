from django.db import models
from django.contrib.auth.models import AbstractUser
from .abstracts import TimeStampedModel


class Country(TimeStampedModel):
    """database table for countries"""
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self) -> str:
        return self.title


class User(AbstractUser):
    """override the user table to add country field"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name='users')

    def __str__(self) -> str:
        return self.username