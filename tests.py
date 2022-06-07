from urllib import response
from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World!', 'Passed'
    assert response.status_code == 200, 'Passed'