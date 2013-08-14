from django.contrib import admin
from models import Doctor

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'correo', 'especialidades', 'fecha_registro', 'validado')
	list_filter = ('validado',)
	search_fields = ['nombre', 'especialidades']

admin.site.register(Doctor, DoctorAdmin)