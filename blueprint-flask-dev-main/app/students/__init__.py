from apiflask import APIBlueprint

bp = APIBlueprint('students', __name__)

from app.students import routes