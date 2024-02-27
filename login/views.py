from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from .models import DadosRegistro
from django.contrib import messages



def register(request):
    
    formulario = RegisterForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect(reverse("login:login"))
    
    template = "login/register.html"
    context = {
        "formulario": formulario,
        "action": "Register",
    }

    return render(request, template, context)

def login(request):

    formulario = LoginForm(request.POST or None)

    if formulario.is_valid():
    
        user = formulario.cleaned_data["username"]
        senha = formulario.cleaned_data["password"]

        if DadosRegistro.objects.filter(username = user, password = senha).exists():
            return HttpResponseRedirect(reverse("page:index"))     
        else:
            messages.error(request, "Usuário ou senha incorretos, tente novamentte. ")
    else:
        LoginForm()

    template = "login/login.html"
    context = {
        "formulario": formulario,
        "action": "Login"
    }

    return render(request, template, context)
            
