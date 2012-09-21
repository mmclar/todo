from piston.handler import BaseHandler
from todo.api import List, Item

class ListHandler(BaseHandler):
    model = List
    allowed_methods = ('PUT', 'DELETE',)
