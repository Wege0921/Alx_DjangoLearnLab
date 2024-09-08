from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete a book
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete a book
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete a book
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),  # Update an existing book
]

