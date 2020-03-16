from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'eventos_del_mes', views.Eventos_Del_MesViewSet)
router.register(r'data_source', views.Data_SourceViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]