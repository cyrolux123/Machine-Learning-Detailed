## Put and Delete - HTTP Verbs
## Working With API's -- JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data in my to do list
items = [
    {
        "id" : 1,
        "name" : "Task 1",
        "description" : "This is task 1"
    },
    {
        "id" : 2,
        "name" : "Task 2",
        "description" : "This is task 2"
    }
]

@app.route("/")
def home():
    return "Welcome to the To Do List!"

# Get: Retrieve all the tasks
@app.route("/items", methods = ["GET"])
def get_items():
    return jsonify(items)

# Get: Retrieve a specific task by id
@app.route("/items/<int:id>", methods = ["GET"])
def get_item(id):
    item = next((item for item in items if item['id'] == id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

# Post: Add a new task
@app.route("/items", methods = ["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item = {
        "id" : items[-1]['id'] + 1 if items else 1,
        "name" : request.json['name'],
        "description" : request.json['description']
    }
    items = items.append(new_item)
    return jsonify(new_item)

# Put: Update a task
@app.route("/items/<int:id>", methods = ["PUT"])
def update_item(id):
    item = next((item for item in items if item['id'] == id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete: Delete a task
@app.route("/items/<int:id>", methods = ["DELETE"])
def delete_item(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({"result":"Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)