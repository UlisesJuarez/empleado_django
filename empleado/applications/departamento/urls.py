
from django.urls import path
from . import views

app_name="departamento_app"

urlpatterns = [
    path('new_depto/',views.NewDeptoView.as_view(),name='nuevo_depto'),
    path('list_depto/',views.DepartamentoListView.as_view(),name="lista_departamentos"),


]
