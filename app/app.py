from operator import methodcaller
from flask import Flask, render_template, url_for, request, redirect
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# OOP structure to store tasks/data in an SQLite database (test.db)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False) # limits task content to 300 characters per post
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # dunder method to view tasks in CLI
    def __repr__(self):
        return f"Todo('{self.id}', '{self.date_created}')"

# Home page & to add tasks
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'] # input
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task) # adds post to database
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding your task."
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

# Page to delete tasks
@app.route('/delete/<int:id>')
def delete(id):
    task_to_del = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_del)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task."

# Page to update tasks
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content'] # overwrites

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task."

    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")