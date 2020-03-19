from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
from .views import(
    Eventos_Del_MesCreateView,
    Eventos_Del_MesUpdateView,
    Eventos_Del_MesDeleteView,
    Eventos_Del_MesListView,
    Data_SourceCreateView,
    Data_SourceUpdateView,
    Data_SourceDeleteView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api-eventos_del_mes', views.Eventos_Del_MesViewSet)
router.register(r'data_source', views.Data_SourceViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('crear_eventos_del_mes/', Eventos_Del_MesCreateView.as_view(), name='eventos_del_mes_crear'),
    path('eventos_del_mes/<int:pk>/editar/', Eventos_Del_MesUpdateView.as_view(), name='eventos_del_mes_editar'),
    path('eliminar_eventos_del_mes/<int:pk>/', Eventos_Del_MesDeleteView.as_view(), name='eventos_del_mes_eliminar'),
    path('eventos_del_mes/', Eventos_Del_MesListView.as_view(), name='eventos_del_mes'),
    path('crear_data_source/', Data_SourceCreateView.as_view(), name='data_source_crear'),
    path('data_source/<int:pk>/editar/', Data_SourceUpdateView.as_view(), name='data_source_editar'),
    path('eliminar_data_source/<int:pk>/', Data_SourceDeleteView.as_view(), name='data_source_eliminar'),
]