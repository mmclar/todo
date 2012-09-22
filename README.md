Description
-----------
A small API for storing lists of todo items.

Requirements
------------
  * Python
  * Django >= 1.4

Setup
-----
To set up the project, clone the repository and run the following in the base folder:

`
./init.sh  
python manage.py syncdb
`  

This will check out an updated version of piston and create the database for the project.

Usage
-----
To start the server use the command `python manage.py runserver`.

You can add a list to the database with the `/api/lists/` endpoint, using JSON to represent the object.  
Example:  
`
url: http://localhost:8000/api/lists/  
verb: POST  
data: { "title": "new list title" }
`  
The response will be the list object that was added, including the ID of the list.  

You can add a todo item by using the `/api/items/` endpoint.
Example:  
`
url: http://localhost:8000/api/items/  
verb: POST  
data: {"list_id": 1, "text": "do something awesome", "dueDate": "2012-09-25"}
`  

You can get a list of all todo items using the `/api/items/` endpoint.  
Example:
`
url: http://localhost:8000/api/items/  
verb: GET  
`  

You can query todo items by using addedDate or dueDate parameters on the `/api/items/` endpoint.  
Example:  
`
url: http://localhost:8000/api/items/?dueDate=2012-09-25  
verb: GET  
`  
will return all of the todo items due on September 25, 2012.
