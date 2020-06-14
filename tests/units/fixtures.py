from pytest import fixture
from goatpig.hello import app

@fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
    return
