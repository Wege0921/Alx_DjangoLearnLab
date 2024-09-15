

from django.db import models
from django.contrib.auth.models import User  # Importing the User model for author field

# Blog Post Model
class Post(models.Model):
    title = models.CharField(max_length=200)  # Field for the post title
    content = models.TextField()  # Field for the post content
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Field to link the post to a user (author)
    published_date = models.DateTimeField(auto_now_add=True)  # Field to store the date and time the post was published

    # To return a readable title in Django admin or when queried
    def __str__(self):
        return self.title

# Create your models here.
