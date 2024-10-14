from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from djongo import models
from bson import ObjectId


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class UserLog(models.Model):
    id = models.ObjectIdField(default=ObjectId, editable=False, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    page_url = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField()

    def __str__(self):
        return f"User {self.user_id} performed {self.action} at {self.timestamp}"
