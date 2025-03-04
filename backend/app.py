from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__) #creates flask application instance, __name__ is the name of the current module
CORS(app) #allows fronend to make requests to backend

todolist = [] #stores todo items

@app.route('/')
def homepage():
    return "Successful Launch!"

@app.route('/api/todos', methods=["GET"]) #maps a url to a python function, route only allows HTTP GET requests
def gatherthetodos():
    return jsonify(todolist)

@app.route('/api/todos', methods=["POST"]) #maps a url to a python function, route only allows HTTP POST requests
def addthetodos():
    data = request.json #gets the JSON data from the request
    todo = {'id': len(todolist) + 1, 'task': data['task'], 'completed': False} #creates a new todo item using a dictionary
    todolist.append(todo) #adds the new todo item to the list
    return jsonify(todo), 201  # Return new task with status 201 (Created)
    
@app.route('/api/todos/<int:todo_id>', methods=["PUT"])
def updatetodo(todo_id):
    data = request.json
    for todo in todolist:
        if todo['id'] == todo_id:
            todo['task'] = data.get('task', todo['task'])
            todo['completed'] = data.get('completed', todo['completed'])
            return jsonify(todo),  200
        else:
            return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:todo_id>', methods=["DELETE"])
def deletetodo(todo_id):
    global todolist
    for todo in todolist:
        if todo['id'] == todo_id:
            todolist.remove(todo)
            return jsonify({'message': 'Todo deleted'}), 200
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)