from django.contrib import admin
from citas.models import Centro,Especialidad,Medico,Prevision,Paciente,Reserva

# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id_rut','nombres','paterno','materno','especialidad')

admin.site.register(Centro)
admin.site.register(Especialidad)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Prevision)
admin.site.register(Paciente)
admin.site.register(Reserva)