from app.courses import bp
from app.extensions import db
from app.models.course import Course, CourseIn, CourseOut
from app.models.student import Student, StudentOut 
from app.models.registration import RegistrationStudentIn



####
## view functions
####    
@bp.get('/<int:course_id>')
@bp.output(CourseOut)
def get_course(course_id):
    return db.get_or_404(Course, course_id)

@bp.get('/')
@bp.output(CourseOut(many=True))
def get_courses():
    return Course.query.all()

@bp.post('/')
@bp.input(CourseIn, location='json')
@bp.output(CourseOut, status_code=201)
def create_course(json_data):
    course = Course(**json_data)
    db.session.add(course)
    db.session.commit()
    return course

@bp.patch('/<int:course_id>')
@bp.input(CourseIn(partial=True), location='json')
@bp.output(CourseOut)
def update_course(course_id, json_data):
    course = db.get_or_404(Course, course_id)
    for attr, value in json_data.items():
        setattr(course, attr, value)
    db.session.commit()
    return course

@bp.delete('/<int:course_id>')
@bp.output({}, status_code=204)
def delete_course(course_id):
    course = db.get_or_404(Course, course_id)
    db.session.delete(course)
    db.session.commit()
    return ''

# register a student with a course
@bp.post('/<int:course_id>/students')
@bp.input(RegistrationStudentIn, location='json')
@bp.output(CourseOut, status_code=201)
def register_student(course_id, json_data):
    course = db.get_or_404(Course, course_id)
    student = db.get_or_404(Student, json_data.get('student_id'))
    course.students.append(student)
    db.session.commit()
    return course

# get all students of a course
@bp.get('/<int:course_id>/students')
@bp.output(StudentOut(many=True))
def get_course_students(course_id):
    course = db.get_or_404(Course, course_id)
    students = course.students
    return students