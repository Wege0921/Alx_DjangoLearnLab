# The Author model represents an individual author who may have written multiple books.
# Each author has a name field to store their full name.

# The Book model represents a book written by an author.
# Each book has a title, a publication year, and a foreign key linking it to an author.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

