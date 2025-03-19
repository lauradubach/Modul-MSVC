from apiflask import APIBlueprint

bp = APIBlueprint('courses', __name__)

from app.courses import routes