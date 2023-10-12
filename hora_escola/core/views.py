from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import CadastroForm
from django.views.decorators.http import require_POST


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# def cadastro(request):
#     template = loader.get_template('cadastro.html')
#     return HttpResponse(template.render())

def cadastro(request):
    context = {}
    context['form'] = CadastroForm()
    return render(request, "cadastro_copy.html", context)

@require_POST
def processar_formulario(request):
    form = CadastroForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Cadastro efetuado com sucesso.")
    return render(request, "500.html")

# -------- HTTP ERROR PAGES --------

def handler400(request, exception):
    template = loader.get_template('400.html')
    return HttpResponse(template.render())

def handler401(request, exception):
    template = loader.get_template('401.html')
    return HttpResponse(template.render())

def csrf_failure(request, reason=""): #Renderiza a página referente ao erro 403
    template = loader.get_template('403.html')
    return HttpResponse(template.render())

def handler404(request, exception):
     template = loader.get_template('404.html')
     return HttpResponse(template.render())

def handler500(request, exception=None):
    template = loader.get_template('500.html')
    context = {}
    return HttpResponse(template.render(context, request))




