from test import client
 
def test_test_page(client):
    response = client.get("/")
    assert response.json['message'] == 'Testing the Flask Application Factory Pattern'
 
def test_get_students(client):
    response = client.get("/students/")
    assert response.json[4]['name'] == 'Mega Tron'
 
def test_get_students_by_id(client):
    response = client.get("/students/4")
    assert response.json['name'] == 'Saad Maan'
 
def test_post_student(client):
    response = client.post("/students/", json={
            'name': 'Nina Hagen', 'level': 'AP'
        })
    assert response.status_code == 201
 
def test_delete_student(client):
    response = client.delete("/students/1")
    assert response.status_code == 204
 
def test_patch_student(client):
    response = client.patch("/students/2", json={
            'name': 'Sam Sung', 'level': 'HF'
        })
    assert response.json['name'] == 'Sam Sung'
    
def test_post_student_course(client):
    response = client.post("/students/2/courses", json={
            "course_id": 3
        })
    assert response.status_code == 201
 
def test_get_student_course(client):
    client.post("/students/2/courses", json={
            "course_id": 3
        })
    response = client.get("/students/2/courses")
    print (response.json)
    assert response.json[0]['title'] == 'M347 Kubernetes'
 
def test_get_courses(client):
    response = client.get("/courses/")
    assert response.json[0]['title'] == 'M231 Security'
 
def test_get_courses_by_id(client):
    response = client.get("/courses/2")
    assert response.json['title'] == 'M254 BPMN'
 
def test_post_course(client):
    response = client.post("/courses/", json={
            'title': 'M100 Networking'
        })
    assert response.status_code == 201
 
def test_delete_course(client):
    response = client.delete("/courses/1")
    assert response.status_code == 204
 
def test_patch_course(client):
    response = client.patch("/courses/2", json={
            'title': 'M254 BPMN'
        })
    assert response.json['title'] == 'M254 BPMN'
 
def test_post_course_student(client):
    response = client.post("/courses/1/students", json={
            "student_id": 1
        })
    assert response.status_code == 201
 
def test_get_course_student(client):
    client.post("/courses/1/students", json={
            "student_id": 2
        })
    response = client.get("/courses/1/students")
    print (response.json)
    assert response.json[0]['name'] == 'Sam Sung'
 