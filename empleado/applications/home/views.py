from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

class IndexView(TemplateView):
    template_name = 'home/home.html'


class pruebaListView(ListView):
    template_name="home/lista.html"
    queryset=["Maria","Dalida","Angeles"]
    context_object_name="lista_prueba"


class pruebasListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name='lista_prueba'



class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    #fields=["titulo","subtitulo","cantidad"]
    #createview tambien acepta un form_class en lugar de fields
    form_class=PruebaForm
    success_url="/"

