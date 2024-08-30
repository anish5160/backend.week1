from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# A list to store to-do items (in-memory)
todos = []
next_id = 1

@csrf_exempt  # Disable CSRF for simplicity
def todo_list(request):
    global next_id

    if request.method == 'GET':
        # Return all to-do items
        return JsonResponse(todos, safe=False)

    elif request.method == 'POST':
        # Add a new to-do item
        data = json.loads(request.body)
        todo = {
            'id': next_id,
            'title': data['title'],
            'completed': False,
        }
        todos.append(todo)
        next_id += 1
        return JsonResponse(todo, status=201)

@csrf_exempt
def todo_detail(request, id):
    global todos

    if request.method == 'DELETE':
        # Remove a to-do item by ID
        todos = [todo for todo in todos if todo['id'] != id]
        return JsonResponse({'message': 'Deleted'}, status=204)

#Invoke-RestMethod in PowerShell is a command-line tool that allows you to interact with web APIs by sending various types of HTTP requests, similar to Postman but without the graphical interface. It’s useful for automating tasks and scripting API interactions directly from the command line.