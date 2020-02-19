from django.urls import path
from .views import crawler

# Crawler url here
urlpatterns = [
    path('<str:placa>', crawler, name="crawler")
]
 