
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
)

#modelos
from .models import Empleado

#importamos nuestro formulario
from .forms import EmpleadoForm

# 1.- Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name="persona/list_all.html"

    """ListView divide los resultados de los registros en 4 eso con la palabra reservada page=numero esto mediante
    una petición de tipo get"""
    paginate_by=5
    ordering='first_name'
    context_object_name="empleados"
    #model=Empleado

    def get_queryset(self):
        palabra_clave=self.request.GET.get("palabra","")
        lista=Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

    #context_object_name='lista'


# 2.- Listar todos los empleados que pertenecen a una area de la empresa
class ListByArea(ListView):
    template_name="persona/list_area.html"
    # queryset=Empleado.objects.filter(
    #     ##departamento igual a la instancia actual en la clase Empleado ponemos '__' nombre del atributo por el que
    #     ##se quiere filtrar
    #     departamento__short_name='Contabilidad'
    # )
    context_object_name="empleados"
    def get_queryset(self):

        area=self.kwargs['short_name']
        lista=Empleado.objects.filter(
        departamento__short_name=area
        )
        return lista

#3.- listar los empleados por trabajo
class ListByJob(ListView):
    template_name="persona/list_job.html"
    context_object_name='lista_jobs'
    
    def get_queryset(self):
        job=self.kwargs['job_name']
        lista=Empleado.objects.filter(
            job=job
        )
        return lista


#4.- listar los empleados por una palabra clave
class ListEmpleadosByKWord(ListView):
    template_name='persona/list_bykword.html'
    context_object_name="empleados"

    def get_queryset(self):
        palabra_clave=self.request.GET.get("palabra","")

        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )

        return lista


#5.- Listar habilidades de un empleado
class ListHabilidadesEmp(ListView):
    template_name="persona/habilidades.html"
    context_object_name='habilidades'
    #el atributo habilidades es many to many

    def get_queryset(self):
        #recupera un unico registro de la bd
        empleado=Empleado.objects.get(id=1)
        return empleado.habilidades.all()


"""La vista generica DetailView"""


class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = "persona/empleado_detalle.html"
    #para que el detail view funcione necesita forsozamente un argumento que sea pk
    
    #este metodo nos sirve para enviar alguna variable extra hacia el template
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetail, self).get_context_data(**kwargs)
        #todo un proceso
        context['titulo']="Empleado del mes"
        return context
    

"""Esta vista solo funciona con un template"""
class successAddEmpleado(TemplateView):
    template_name = "persona/success.html"



"""La vista generica CreateView utilizada para ingresar registros en el modelo de base datos"""
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add_empleado.html"
    
    #atributos del modelo que queremos que se filtren en pantalla
    #fields=["first_name","last_name","job","departamento","habilidades","avatar"]
    form_class=EmpleadoForm
    
    #para no hacer uno por uno lo hacemos de la siguiente manera
    #fields=("__all__")

    #para ver el formulario con el input para estos campos utilizamos la palabra reservada 'form'

    #si quiero que se recarge en la misma pagina
    #success_url="."

    #no es recomendable hardcodear las urls
    #success_url="/success"
    
    success_url=reverse_lazy('persona_app:empleados_all')

    def form_valid(self, form):
        empleado=form.save(commit=False)
        empleado.full_name=empleado.first_name+" "+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)
    

"""UpdateView"""

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields=["first_name","last_name","job","departamento","habilidades"]

    success_url=reverse_lazy('persona_app:lista_admin')

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        print(request.POST)
        print(request.POST["last_name"])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):

        return super(EmpleadoUpdateView,self).form_valid(form)
    
    #primero se ejecuta el post y luego el form_valid


"""DeleteView"""

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url=reverse_lazy('persona_app:lista_admin')



"""Vista que carga la pagina de inicio"""
class InicioView(TemplateView):
    template_name = "inicio.html"



class ListaEmpleadosAdmin(ListView):
    template_name="persona/lista_admin.html"
    paginate_by=10
    ordering='first_name'
    context_object_name="empleados"
    model=Empleado