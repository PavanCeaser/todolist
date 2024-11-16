from flask import Flask, render_template, request, redirect, url_for
import couchdb,os

# Initialize the Flask app
app = Flask(__name__)

# Connect to CouchDB
couch = couchdb.Server('http://127.0.0.1:5984/')  # Replace with your CouchDB URL if different
db = couch.create('todolist') if 'todolist' not in couch else couch['todolist']

@app.route('/')
def index():
    # Fetch all tasks from the CouchDB database
    tasks = [task for task in db.view('_all_docs', include_docs=True)]
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        # Add a new task to CouchDB
        doc = {
            'task': task_name,
            'completed': False
        }
        db.save(doc)
    return redirect(url_for('index'))

@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    # Delete task from CouchDB
    task = db[task_id]
    db.delete(task)
    return redirect(url_for('index'))

@app.route('/complete/<task_id>', methods=['POST'])
def complete_task(task_id):
    # Mark a task as completed
    task = db[task_id]
    task['completed'] = True
    db.save(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
