from django.shortcuts import render

# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})



from django.views.generic import DetailView
from .models import Library

# relationship_app/views.py
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# relationship_app/views.py

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# relationship_app/views.py

from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

