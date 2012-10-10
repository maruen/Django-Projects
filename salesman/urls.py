from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',

     (r'^register/', include('salesman.register.urls')),

     (r'^admin/',    include(admin.site.urls)),

     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

     (r'media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
     
     )
