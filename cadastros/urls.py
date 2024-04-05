from django.urls import path
from .views import ClienteCreate, EntregaCreate
from .views import EntregaUpdate
from .views import EntregaDelete
from .views import EntregaList

urlpatterns = [
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('cadastrar/entrega/', EntregaCreate.as_view(), name='cadastrar-entrega'),


    path('editar/entrega/<int:pk>/', EntregaUpdate.as_view(), name='editar-entrega'),

    path('excluir/entrega/<int:pk>/', EntregaDelete.as_view(), name='excluir-entrega'),

    path('listar/entrega', EntregaList.as_view(), name='listar-entrega'),

]
