from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(100))

    def save_task_to_db(self):
        self.id = Todo.id
        self.details = Todo.details

