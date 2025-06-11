import json
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = 'todos.json'

# Allow embedding in iframes
@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    return response

# In-memory storage for todos
# タスクに優先度(priority)を追加
todos = []

# ファイルからタスクを読み込む関数
def load_todos():
    global todos
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            todos = json.load(f)
    else:
        todos = []

# ファイルにタスクを保存する関数
def save_todos():
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    # 優先度でソートして表示
    sorted_todos = sorted(todos, key=lambda x: x.get('priority', 0))
    return render_template('index.html', todos=sorted_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    global todos
    task = request.form.get('task')
    if task:
        # 追加時の優先度は最大値+1に設定
        max_priority = max([todo.get('priority', 0) for todo in todos], default=0)
        todos.append({'task': task, 'completed': False, 'priority': max_priority + 1})
        save_todos()
    return index()

@app.route('/toggle', methods=['POST'])
def toggle_todo():
    global todos
    task_index = request.json.get('index')
    if task_index is not None and 0 <= task_index < len(todos):
        todos[task_index]['completed'] = not todos[task_index]['completed']
        save_todos()
        return jsonify({'success': True, 'completed': todos[task_index]['completed']})
    return jsonify({'success': False}), 400

@app.route('/delete', methods=['POST'])
def delete_todo():
    global todos
    task_index = request.json.get('index')
    if task_index is not None and 0 <= task_index < len(todos):
        todos.pop(task_index)
        save_todos()
        return jsonify({'success': True})
    return jsonify({'success': False}), 400

@app.route('/reorder', methods=['POST'])
def reorder_todos():
    global todos
    new_order = request.json.get('order')
    if not isinstance(new_order, list) or len(new_order) != len(todos):
        return jsonify({'success': False, 'message': 'Invalid order data'}), 400

    try:
        # new_orderはタスクのインデックスの新しい順序のリスト
        reordered = [todos[i] for i in new_order]
        # 優先度を並び順に更新
        for i, todo in enumerate(reordered):
            todo['priority'] = i
        todos = reordered
        save_todos()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    load_todos()
    app.run(host='0.0.0.0', port=9111, debug=True, use_reloader=False)
