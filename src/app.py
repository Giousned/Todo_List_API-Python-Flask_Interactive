from flask import Flask
from flask import json, jsonify
from flask import request

app = Flask(__name__)

# def hello_world():
#     # supongamos que tienes some_data (cierta información) en una variable json
#     some_data = { "name": "Bobby", "lastname": "Rixer" }

#     # puedes convertir esa variable en un string json así
#     json_text = jsonify(some_data)

#     # y luego puedes retornarla (return) en el response body así:
#     return json_text



todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
     
    json_todos = jsonify(todos)

    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # request_body = request.json  # OTRA FORMA
    
    # OTRA FORMA
    # request_body = request.data 
    # decoded_object = json.loads(request_body)
    # todos.append(decoded_object)

    request_body = request.get_json(force=True)

    todos.append(request_body)

    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.remove(todos[position])
    print("This is the position to delete: ",position)
    return jsonify(todos)



# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)