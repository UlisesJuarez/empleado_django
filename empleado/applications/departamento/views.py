from django.http import HttpResponse
from django.shortcuts import render

from applications.persona.models import Empleado
from .models import Departamento

#para hacer createViews que no dependan de un modelo
from django.views.generic.edit import FormView

#importar el formulario que haya creado
from .forms import NewDepartamentoForm

from django.views.generic import (ListView)

class NewDeptoView(FormView):
    template_name="departamento/new_depto.html"
    form_class=NewDepartamentoForm
    success_url="/"

    def form_valid(self, form):
        #instancia de departamento
        depa=Departamento(
            name=form.cleaned_data["departamento"],
            short_name=form.cleaned_data['short_name']
        )

        depa.save()

        nombre=form.cleaned_data["nombre"]
        apellido=form.cleaned_data["apellidos"]
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job=1,
            departamento=depa)
        return super(NewDeptoView,self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista_deptos.html"
    context_object_name="departamentos"
