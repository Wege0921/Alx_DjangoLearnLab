from django.urls import include, path

urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),
    # other paths...
]

