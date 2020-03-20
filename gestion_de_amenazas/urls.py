from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
from .views import(
    Amenazas_Del_MesCreateView,
    Amenazas_Del_MesUpdateView,
    Amenazas_Del_MesDeleteView,
    Amenazas_Del_MesListView,
    Alerta_AmenazaCreateView,
    Alerta_AmenazaUpdateView,
    Alerta_AmenazaDeleteView,
    Tendencia_AmenazaCreateView,
    Tendencia_AmenazaUpdateView,
    Tendencia_AmenazaDeleteView,
    Grafico_Lineas_Tendencia_AmenazasCreateView,
    Grafico_Lineas_Tendencia_AmenazasUpdateView,
    Grafico_Lineas_Tendencia_AmenazasDeleteView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api-amenazas_del_mes', views.Amenazas_Del_MesViewSet)
router.register(r'api-alerta_amenaza', views.Alerta_AmenazaViewSet)
router.register(r'api-tendencia_amenaza', views.Tendencia_AmenazaViewSet)
router.register(r'api-grafico_lineas_tendencia_amenazas', views.Grafico_Lineas_Tendencia_AmenazasViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # amenazas_del_mes
    path('crear_amenazas_del_mes/', Amenazas_Del_MesCreateView.as_view(), name='amenazas_del_mes_crear'),
    path('amenazas_del_mes/<int:pk>/editar/', Amenazas_Del_MesUpdateView.as_view(), name='amenazas_del_mes_editar'),
    path('eliminar_amenazas_del_mes/<int:pk>/', Amenazas_Del_MesDeleteView.as_view(), name='amenazas_del_mes_eliminar'),
    path('amenazas_del_mes/', Amenazas_Del_MesListView.as_view(), name='amenazas_del_mes'),
    # alerta_amenaza
    path('crear_alerta_amenaza/', Alerta_AmenazaCreateView.as_view(), name='alerta_amenaza_crear'),
    path('alerta_amenaza/<int:pk>/editar/', Alerta_AmenazaUpdateView.as_view(), name='alerta_amenaza_editar'),
    path('eliminar_alerta_amenaza/<int:pk>/', Alerta_AmenazaDeleteView.as_view(), name='alerta_amenaza_eliminar'),
    #  tendencia_amenaza
    path('crear_tendencia_amenaza/', Tendencia_AmenazaCreateView.as_view(), name='tendencia_amenaza_crear'),
    path('tendencia_amenaza/<int:pk>/editar/', Tendencia_AmenazaUpdateView.as_view(), name='tendencia_amenaza_editar'),
    path('eliminar_tendencia_amenaza/<int:pk>/', Tendencia_AmenazaDeleteView.as_view(), name='tendencia_amenaza_eliminar'),
    #  grafico_lineas_tendencia_amenazas
    path('crear_grafico_lineas_tendencia_amenazas/', Grafico_Lineas_Tendencia_AmenazasCreateView.as_view(), name='grafico_lineas_tendencia_amenazas_crear'),
    path('grafico_lineas_tendencia_amenazas/<int:pk>/editar/', Grafico_Lineas_Tendencia_AmenazasUpdateView.as_view(), name='grafico_lineas_tendencia_amenazas_editar'),
    path('eliminar_grafico_lineas_tendencia_amenazas/<int:pk>/', Grafico_Lineas_Tendencia_AmenazasDeleteView.as_view(), name='grafico_lineas_tendencia_amenazas_eliminar'),
]