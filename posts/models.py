"""Posts models."""

# Django
from django.db import models


class User(models.Model):
    """User model."""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return email."""
        return self.email