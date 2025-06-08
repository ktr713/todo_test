from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Allow embedding in iframes
@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    return response

# In-memory storage for todos
todos = []

@app.route('/')
def index():
    html = '''
    <html>
    <head>
        <title>ToDo App</title>
    </head>
    <body>
        <h1>ToDo List</h1>
        <ul>
            %s
        </ul>
        <form action="/add" method="post">
            <input type="text" name="task" placeholder="New Task" required>
            <button type="submit">Add Task</button>
        </form>
    </body>
    </html>
    '''
    list_items = ''.join([f"<li>{task}</li>" for task in todos])
    return html % list_items

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51140, debug=True)
