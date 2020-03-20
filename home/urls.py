from django.urls import path, include
from . import views
from .views import(
    HomeView,
)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]