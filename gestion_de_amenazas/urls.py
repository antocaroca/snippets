from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'amenazas_del_mes', views.Amenazas_Del_MesViewSet)
router.register(r'alerta_amenaza', views.Alerta_AmenazaViewSet)
router.register(r'tendencia_amenaza', views.Tendencia_AmenazaViewSet)
router.register(r'grafico_lineas_tendencia_amenazas', views.Grafico_Lineas_Tendencia_AmenazasViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]