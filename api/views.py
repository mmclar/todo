from piston.handler import BaseHandler
from api.models import List, Item

class ListHandler(BaseHandler):
    model = List
    allowed_methods = ('PUT', 'DELETE',)

class ItemHandler(BaseHandler):
    model = Item
    allowed_methods = ('PUT', 'DELETE',)
