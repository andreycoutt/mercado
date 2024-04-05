from django.urls import path
from .views import IndexView, SobreView, CadastrarEntregaView, ListarEntregasView


urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cadastrar/', CadastrarEntregaView.as_view(), name='cadastrarentrega'),
    path('listar/', ListarEntregasView.as_view(), name='listarentregas'),
    
]