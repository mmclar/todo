from piston.handler import BaseHandler
from api.models import List, Item
import simplejson
from datetime import date
from piston.utils import Mimer
Mimer.register(simplejson.loads, ('application/json', 'application/json; charset=UTF-8',))

class ListHandler(BaseHandler):
    model = List
    allowed_methods = ('POST', 'PUT', 'DELETE', 'GET')
    fields = ('id', 'title')

def date_from_param(request, param):
    d = request.GET.get(param, None)
    if d:
        parts = d.split('-')
        d = date(int(parts[0]), int(parts[1]), int(parts[2]))
    return d

class ItemHandler(BaseHandler):
    model = Item
    allowed_methods = ('POST', 'PUT', 'DELETE', 'GET',)

    def read(self, request):
        due_date = date_from_param(request, 'dueDate')
        added_date = date_from_param(request, 'addedDate')
        matches = Item.objects.all()
        if due_date:
            matches = matches.filter(dueDate=due_date)
        if added_date:
            matches = matches.filter(addedDate=added_date)
        return matches

