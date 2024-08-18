from django.urls import include, path


# relationship_app/urls.py
from django.urls import path
from .views import LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/', include('relationship_app.urls')),
    # Other URL patterns
]

