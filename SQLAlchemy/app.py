from apiflask import APIFlask, Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask_sqlalchemy import SQLAlchemy
import os

app = APIFlask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


######
# Data Models

# Hilfstabelle für many to many Relation
student_course_association = db.Table(
    'student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('courses.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('students.id'))
)

# für SQL Alchemy (table definition)

## course DB Schema und In/Out Schemas
class CourseModel(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(8))
    students = db.relationship('StudentModel', secondary=student_course_association, back_populates='courses') 

class CourseIn(Schema):
    title = String(required=True, validate=Length(0, 32))
   
class CourseOut(Schema):
    id = Integer()
    title = String()

## student DB Schema und In/Out Schemas
class StudentModel(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    level = db.Column(db.String(8))
    courses = db.relationship('CourseModel', secondary=student_course_association, back_populates='students') 

class StudentIn(Schema):
    name = String(required=True, validate=Length(0, 32))
    level = String(required=True, validate=OneOf(['HF', 'PE', 'AP', 'ICT']))

class StudentOut(Schema):
    id = Integer()
    name = String()
    level = String()

class RegistrationIn(Schema):
    course_id = Integer()


# Hilfsfunktion (Testdaten erstellen, Tabellen erstellen)
def init_database():
    db.drop_all() # dieser Befehl löscht alle vorhandenen Datenbankeintraege und Tabellen
    db.create_all()

    # Beispieldaten
    students = [
        {'name': 'Freda Kids', 'level': 'HF'},
        {'name': 'Sam Sung', 'level': 'HF'},
        {'name': 'Chris P. Bacon', 'level': 'AP'},
        {'name': 'Saad Maan', 'level': 'PE'}
    ]
    for student_data in students:
        student = StudentModel(**student_data)
        db.session.add(student)

    courses = [
        {'title': 'M321'},
        {'title': 'M123'}
    ]
    for course_data in courses:
        course = CourseModel(**course_data)
        db.session.add(course)

    db.session.commit()


@app.get('/')
def say_hello():
    return {'message': 'Hello - I am a complex SQLAlchemy Example with APIFlask!'}


@app.get('/students/<int:student_id>')
@app.output(StudentOut)
def get_student(student_id):
    return db.get_or_404(StudentModel, student_id)


@app.get('/students')
@app.output(StudentOut(many=True))
def get_students():
    return StudentModel.query.all()


@app.post('/students')
@app.input(StudentIn, location='json')
@app.output(StudentOut, status_code=201)
def create_student(json_data):
    student = StudentModel(**json_data)
    db.session.add(student)
    db.session.commit()
    return student


@app.patch('/students/<int:student_id>')
@app.input(StudentIn(partial=True), location='json')
@app.output(StudentOut)
def update_student(student_id, json_data):
    student = db.get_or_404(StudentModel, student_id)
    for attr, value in json_data.items():
        setattr(student, attr, value)
    db.session.commit()
    return student


@app.delete('/students/<int:student_id>')
@app.output({}, status_code=204)
def delete_student(student_id):
    student = db.get_or_404(StudentModel, student_id)
    db.session.delete(student)
    db.session.commit()
    return ''


# register a student with a course
@app.post('/students/<int:student_id>/courses')
@app.input(RegistrationIn, location='json')
@app.output(StudentOut, status_code=201)
def register_student(student_id, json_data):
    student = db.get_or_404(StudentModel, student_id)
    course = db.get_or_404(CourseModel, json_data.get('course_id'))
    student.courses.append(course)
    course.students.append(student)
    db.session.commit()
    return student


# get all courses of a student
@app.get('/students/<int:student_id>/courses')
@app.output(CourseOut(many=True))
def get_student_courses(student_id):
    student = db.get_or_404(StudentModel, student_id)
    courses = student.courses
    return courses


with app.app_context():
    init_database()
