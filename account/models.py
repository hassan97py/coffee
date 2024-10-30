from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    # تنظیم related_name برای جلوگیری از تداخل
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # تغییر نام به customuser_set
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # تغییر نام به customuser_set
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

