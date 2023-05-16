from django.urls import path
from . import views


app_name="persona_app"

urlpatterns = [
    path(
                'listar_all_empleados/',
                views.ListAllEmpleados.as_view(),
                name='empleados_all'),
    path(
                'listar_by_area/<short_name>/',
                views.ListByArea.as_view(),
                name="empleado_area"),
    path(
                'listar_by_job/<job_name>/',
                views.ListByJob.as_view()),
    path(
                'buscar-empleado/',
                views.ListEmpleadosByKWord.as_view()),
    path(       
                'listar_habilidades/',
                views.ListHabilidadesEmp.as_view()),
    path(
                'ver_empleados/<pk>/',
                views.EmpleadoDetail.as_view(),
                name='empleado_detalle'),
    path(
                'nuevo_empleado/',
                views.EmpleadoCreateView.as_view(),
                name='nuevo_empleado'),
    path(
                'success/',views.successAddEmpleado.as_view(),
                name='correcto'),
    path(
                'update/<pk>/',
                views.EmpleadoUpdateView.as_view(),
                name="modificar_empleado"),
    path(
                "delete/<pk>/",
                views.EmpleadoDeleteView.as_view(),
                name="delete_empleado"),
    path(
                '',
                views.InicioView.as_view(),
                name='inicio'),
    path(
                'lista_empleados_admin/',
                views.ListaEmpleadosAdmin.as_view(),
                name='lista_admin'),
]
