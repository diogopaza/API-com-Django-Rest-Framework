from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_consultas_medicas.api import viewsets 


router = routers.DefaultRouter()
router.register(r'pessoa-profissional', viewsets.PessoaProfissionalViewSet, basename="PessoaProfissional")
router.register(r'consultas', viewsets.ConsultaViewSet, basename="Consulta")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),       
    path('consultas-por-profissional/<int:pk>/', viewsets.ConsultasPorProfissionais.as_view()) 
]
