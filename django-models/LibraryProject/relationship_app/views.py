from django.shortcuts import render
# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Library
from django.views.generic.detail import DetailView
# Create your views here.

from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# relationship_app/views.py
# relationship_app/views.py
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

