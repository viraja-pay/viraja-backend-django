from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator

class UserProfile(AbstractUser):
    """
    User model
    """
    phone_regex = RegexValidator(
        regex=r'(\d{3})\D*(\d{3})\D*(\d{4})$',  # r'^d{7,12}$',
        message="Phone Number must be entered in the format: '999999999'. Up to 12 digits allowed."
    )  # r'^\+?1?\d{9,15}$'
    phone = models.CharField(
        max_length=12,
        blank=True,
        validators=[phone_regex]
    )
