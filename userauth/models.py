from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    # Add related_name arguments to the groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userauth_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userauth_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
