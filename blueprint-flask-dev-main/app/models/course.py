from apiflask import Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

from app.extensions import db
from app.models.registration import Registration

class CourseIn(Schema):
    title = String(required=True, validate=Length(0, 32))
   
class CourseOut(Schema):
    id = Integer()
    title = String()

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    students = db.relationship('Student', secondary='registrations', back_populates='courses') 