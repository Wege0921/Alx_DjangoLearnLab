from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    def follow(self, user):
        """Follow another user."""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user."""
        self.following.remove(user)

    def is_following(self, user):
        """Check if the user is following another user."""
        return self.following.filter(id=user.id).exists()

    def __str__(self):
        return self.username

