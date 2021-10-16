# Pizza-API-DRF
### Pizza API Based on Django REST Framework.
### User can Create, List, Update, Delete and Filter API of Pizza
## Third Party Package
- django-filter



## API EndPoints
- Create Regular or Square Pizza:- localhost:8000/pizza/create/
- List All pizza information:- localhost:8000/pizza/list/
- Edit or Delete Pizza:- localhost:8000/pizza/edit-delete/pk of pizza must be integer/ eg. localhost:8000/pizza/edit-delete/2/
- Filter Pizza by pizza type and pizza size:- localhost:8000/pizza/list?pizza_type=Regular&pizza_size=Large 


### Notes: 
-(*All Endpoints have tested with Postman And Django REST Browsable API*)
- (*dont't forget to add slash in last of every Endpoints except Filter endpoint.*)
- (*Create API endpoints http method POST*)
- (*List API endpoints http method GET*)
- (*Edit or Delete API endpoints http method PUT*)
- (*Filter API endpoints http method GET*)

## Steps to Run Project

- Make virtual Environment with command : python -m venv pizza
- Go virtual environment directory with command: cd pizza/scripts
- activate virtual environment with command: ./activate
- go back outside of virtual environment directory with command: cd..
- intall django with command: pip install django
- Create a django project and run requirements.txt with command: pip install -r requirements.txt
- add pizza apps , rest_framework and django_filters in Settings installed app
- run makemigrations and migrate command
- run django server
- hit all Endpoints one by one according to above mention notes.


