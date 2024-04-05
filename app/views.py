from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class CadastrarEntregaView(TemplateView):
    template_name = 'cadastrarentrega.html'

class ListarEntregasView(TemplateView):
    template_name = 'listarentregas.html'