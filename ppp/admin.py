from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Periodo)

admin.site.register(Carta)
admin.site.register(PlanPractica)
admin.site.register(InformePractica)

admin.site.register(HistorialCarta)
admin.site.register(HistorialPlanPractica)
admin.site.register(SolicitudAsesor)
admin.site.register(HistorialInformePractica)