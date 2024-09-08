from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    # /books/ will list all books or create a new one
    path('books/', BookListView.as_view(), name='book-list'),
    
    # /books/<int:pk>/ will retrieve, update, or delete a specific book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]

