from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from backend.api import RecursoDoctor
admin.autodiscover()

doctor_recursos = RecursoDoctor()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'backend.views.inicio'),
    # url(r'^tgbackend/', include('tgbackend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(doctor_recursos.urls))
)
