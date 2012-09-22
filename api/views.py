from piston.handler import BaseHandler
from api.models import List, Item
import simplejson
from piston.utils import Mimer
Mimer.register(simplejson.loads, ('application/json', 'application/json; charset=UTF-8',))

class ListHandler(BaseHandler):
    model = List
    allowed_methods = ('POST', 'PUT', 'DELETE',)

class ItemHandler(BaseHandler):
    model = Item
    allowed_methods = ('POST', 'PUT', 'DELETE',)
