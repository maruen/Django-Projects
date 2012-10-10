from django.conf.urls.defaults import *
from salesman.register.models import Product

info_dict = {
      'queryset': Product.objects.all(),
}


urlpatterns = patterns('',

      (r'^$', 'django.views.generic.list_detail.object_list',info_dict),
      url(r'^user/add/$', 'register.views.edit_user'),
      url(r'^user/(?P<user_id>\d+)/edit/$', 'register.views.edit_user'),
          
)
