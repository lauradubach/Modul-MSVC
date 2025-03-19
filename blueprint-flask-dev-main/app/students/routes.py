from app.students import bp
from app.extensions import db
from app.models.student import Student, StudentIn, StudentOut
from app.models.course import Course, CourseOut
from app.models.registration import RegistrationCourseIn



####
## view functions
####    
@bp.get('/<int:student_id>')
@bp.output(StudentOut)
def get_student(student_id):
    return db.get_or_404(Student, student_id)

@bp.get('/')
@bp.output(StudentOut(many=True))
def get_students():
    return Student.query.all()

@bp.post('/')
@bp.input(StudentIn, location='json')
@bp.output(StudentOut, status_code=201)
def create_student(json_data):
    student = Student(**json_data)
    db.session.add(student)
    db.session.commit()
    return student

@bp.patch('/<int:student_id>')
@bp.input(StudentIn(partial=True), location='json')
@bp.output(StudentOut)
def update_student(student_id, json_data):
    student = db.get_or_404(Student, student_id)
    for attr, value in json_data.items():
        setattr(student, attr, value)
    db.session.commit()
    return student

@bp.delete('/<int:student_id>')
@bp.output({}, status_code=204)
def delete_student(student_id):
    student = db.get_or_404(Student, student_id)
    db.session.delete(student)
    db.session.commit()
    return ''

# register a student with a course
@bp.post('/<int:student_id>/courses')
@bp.input(RegistrationCourseIn, location='json')
@bp.output(StudentOut, status_code=201)
def register_course(student_id, json_data):
    student = db.get_or_404(Student, student_id)
    course = db.get_or_404(Course, json_data.get('course_id'))
    student.courses.append(course)
    db.session.commit()
    return student

# get all courses of a student
@bp.get('/<int:student_id>/courses')
@bp.output(CourseOut(many=True))
def get_student_courses(student_id):
    student = db.get_or_404(Student, student_id)
    courses = student.courses
    return courses