from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import(
    VulnerabilidadListView,
    VulnerabilidadCreateView,
    VulnerabilidadUpdateView,
    VulnerabilidadDetailView,
    VulnerabilidadDeleteView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api-vulnerabilidad', views.VulnerabilidadViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('vulnerabilidad/', views.VulnerabilidadListView.as_view(), name='vulnerabilidad_listar'),
    path('crear_vulnerabilidad/', views.VulnerabilidadCreateView.as_view(), name='vulnerabilidad_crear'),
    path('vulnerabilidad/<int:pk>/editar/', VulnerabilidadUpdateView.as_view(), name='vulnerabilidad_editar'),
    path('vulnerabilidad/<int:pk>/', VulnerabilidadDetailView.as_view(), name='vulnerabilidad_detalle'),
    path('eliminar_vulnerabilidad/<int:pk>/', views.VulnerabilidadDeleteView.as_view(), name='vulnerabilidad_eliminar'),
]