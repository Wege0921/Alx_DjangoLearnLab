

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



# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    # existing fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

# Create your models here.
