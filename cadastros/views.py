from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente, Entrega
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'telefone', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class EntregaCreate(CreateView):
    model = Entrega
    fields = ['nome', 'endereco', 'caixas', 'volumeextra', 'nomeembalador', 'datacompra', 'datahoraentrega']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-entrega')

# update #

class EntregaUpdate(UpdateView):
    model = Entrega
    fields = ['nome', 'endereco', 'caixas', 'volumeextra', 'nomeembalador', 'datacompra', 'datahoraentrega']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-entrega')

# delete #

class EntregaDelete(DeleteView):
    model = Entrega
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-entrega')

# list #

class EntregaList(ListView):
    model = Entrega
    template_name = 'cadastros/listas/entrega.html'