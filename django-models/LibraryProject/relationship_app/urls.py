from django.urls import include, path

urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),
    # other paths...
]


# relationship_app/urls.py
from django.urls import path
from .views import LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Other URL patterns
]

