
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.IndexView.as_view()),
    path('lista/',views.pruebaListView.as_view()),
    path('lista-prueba/',views.pruebasListView.as_view()),
    path('add/',views.PruebaCreateView.as_view(), name="prueba_add"),
]
