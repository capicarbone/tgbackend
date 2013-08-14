# *.* coding: utf-8 *.*

from tastypie.resources import ModelResource
from models import Doctor


class RecursoDoctor(ModelResource):
    class Meta:
        queryset = Doctor.objects.all()
        resource_name = 'doctor'