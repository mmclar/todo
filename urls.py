from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^api/', include('todo.api.urls')),
)
