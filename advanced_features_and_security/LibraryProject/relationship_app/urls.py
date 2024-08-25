from django.urls import include, path


# relationship_app/urls.py
from django.urls import path
from .views import LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/', include('relationship_app.urls')),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    # Other URL patterns
]

