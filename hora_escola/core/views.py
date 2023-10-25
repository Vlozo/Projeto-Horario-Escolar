from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import RegistrationForm
from django.views.decorators.http import require_POST


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def sign_up(request):
    template = 'signUp.html'
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, template, {'form': form})
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    
        else:
            return render(request, template, {'form':form})   

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




