from django.conf.urls.defaults import *
from piston.resource import Resource
from todo.api.views import ListHandler, ItemHandler

urlpatterns = patterns('',
    url(r'^lists/$', Resource(ListHandler)),
    url(r'^items/$', Resource(ItemHandler)),
)
