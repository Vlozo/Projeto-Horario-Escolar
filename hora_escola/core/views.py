from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout 
from .forms import RegistrationForm, AuthenticationFormCustomized

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationFormCustomized(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationFormCustomized()
    return render(request, 'index.html', {'form':form})

def sign_up(request):
    template = 'signUp.html'
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, template, {'form': form})
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('sign_in')
        else:
            return render(request, template, {'form':form})

@login_required
def home(request):
    template = 'home.html'
    return render(request, template)



#  ----- PAGINAS DE ERRO -----

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




