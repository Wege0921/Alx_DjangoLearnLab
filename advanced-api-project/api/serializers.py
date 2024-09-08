# The BookSerializer serializes the Book model, ensuring that the publication year is valid.
# It includes custom validation to prevent setting the publication year in the future.

# The AuthorSerializer serializes the Author model, including a nested BookSerializer
# to dynamically serialize the books written by the author.

from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']

