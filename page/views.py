import django
from django.shortcuts import render, HttpResponseRedirect 
from .models import DadosCard
from django.urls import reverse

def home(request):

    cards = DadosCard.objects.all()
    tarefas_finalizadas = DadosCard.objects.filter(done = True)
    tarefas_a_fazer = DadosCard.objects.filter(done = False)

    template = "page/home.html"
    context = {
        "cards": cards,
        "tarefas_a_fazer": tarefas_a_fazer,
        "tarefas_finalizadas": tarefas_finalizadas,
    }

    return render(request, template, context)

def done(request, tarefa_id):
    tarefa = DadosCard.objects.get(pk = tarefa_id)
    tarefa.make_done()
    return HttpResponseRedirect(reverse("page:home"))