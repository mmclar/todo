

from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ListHandler, ItemHandler

urlpatterns = patterns('',
    url(r'^lists/$', Resource(ListHandler)),
    url(r'^items/$', Resource(ItemHandler)),
)
