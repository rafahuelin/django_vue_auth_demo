from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/avatar.png')

    def __str__(self):
        return f'{self.user.username} (profile)'