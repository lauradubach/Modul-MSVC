from apiflask import APIFlask, Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = APIFlask(__name__, docs_path='/docs')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    level = db.Column(db.String(8))

class StudentIn(Schema):
    name = String(required=True, validate=Length(max=32))
    level = String(required=True, validate=OneOf(['HF', 'AP', 'PE', 'ICT']))
                                                  
class StudentOut(Schema):
    name = String()
    level = String()

with app.app_context():
    db.create_all()

@app.post('/students')
@app.input(StudentIn, location='json')
@app.output(StudentOut, status_code=201)
def create_student(json_data):
    student = StudentModel(**json_data)
    db.session.add(student)
    db.session.commit()
    return student

# Einzelnen Studenten abrufen
@app.get('/students/<int:id>')
@app.output(StudentOut)
def get_student(id):
    student = StudentModel.query.get(id)
    if not student:
        return {"error": "Student not found"}, 404
    return student

# Alle Studenten abrufen
@app.get('/students')
@app.output(StudentOut(many=True))
def get_students():
    students = StudentModel.query.all()
    return students

# Student aktualisieren
@app.put('/students/<int:id>')
@app.input(StudentIn, location='json')
@app.output(StudentOut)
def update_student(id, json_data):
    student = StudentModel.query.get(id)
    if not student:
        return {"error": "Student not found"}, 404
    student.name = json_data["name"]
    db.session.commit()
    return student

# Student löschen
@app.delete('/students/<int:id>')
def delete_student(id):
    student = StudentModel.query.get(id)
    if not student:
        return {"error": "Student not found"}, 404
    db.session.delete(student)
    db.session.commit()
    return {"message": "Student deleted"}, 200


