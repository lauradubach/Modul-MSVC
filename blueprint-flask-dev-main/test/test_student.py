from test import client

def test_get_students(client):
    response = client.get("/students/")
    assert response.json[4]['name'] == 'Mega Tron'

def test_post_student(client):
    response = client.post("/students/", json={
            'name': 'Nina Hagen', 'level': 'AP'
        })
    assert response.status_code == 201

...