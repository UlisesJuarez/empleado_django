from django.contrib import admin
from .models import Empleado, Habilidades


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    # def full_name(self,obj):
    #     #obj pinta el registro completo de cada iteración 
    #     return obj.first_name+" "+obj.last_name

    search_fields=(
        'first_name',
    )
    
    list_filter=('departamento','job',
                'habilidades',)

    #solo funciona para las relaciones muchos a muchos
    filter_horizontal=('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)