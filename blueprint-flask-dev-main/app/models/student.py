from apiflask import Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

from app.extensions import db
from app.models.registration import Registration

####
## Schemas for OpenAPI and validation
####
class StudentIn(Schema):
    name = String(required=True, validate=Length(0, 32))
    level = String(required=True, validate=OneOf(['HF', 'PE', 'AP', 'ICT']))

class StudentOut(Schema):
    id = Integer()
    name = String()
    level = String()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    level = db.Column(db.String(8))
    courses = db.relationship('Course', secondary='registrations', back_populates='students')