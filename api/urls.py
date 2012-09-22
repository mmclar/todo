from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from todo.api.views import ListHandler, ItemHandler

urlpatterns = patterns('',
    url(r'^lists/$', Resource(ListHandler), { 'emitter_format': 'json' }),
    url(r'^items/$', Resource(ItemHandler), { 'emitter_format': 'json' }),
)
