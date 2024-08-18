from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/', include('relationship_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.list_books, name='list_books'),  # assuming list_books exists
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]


# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for adding a book
    path('add_book/', views.add_book, name='add_book'),

    # URL pattern for editing a book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # URL pattern for deleting a book
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Add other URL patterns here
]

