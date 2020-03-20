from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
from .views import(
    HallazgoCreateView,
    HallazgoUpdateView,
    HallazgoDeleteView,
    HallazgoListView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api-hallazgo', views.HallazgoViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('crear_hallazgo/', HallazgoCreateView.as_view(), name='hallazgo_crear'),
    path('hallazgo/<int:pk>/editar/', HallazgoUpdateView.as_view(), name='hallazgo_editar'),
    path('eliminar_hallazgo/<int:pk>/', HallazgoDeleteView.as_view(), name='hallazgo_eliminar'),
    path('hallazgo/', HallazgoListView.as_view(), name='hallazgo_listar'),
]