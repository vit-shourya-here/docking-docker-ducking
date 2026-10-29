
from app import app

client = app.test_client()


def calculate(a, b, op):
    return client.post(
        "/",
        data={"a": str(a), "b": str(b), "op": op}
    )


def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculator V2" in response.get_data(as_text=True)


def test_addition():
    response = calculate(10, 5, "add")
    assert response.status_code == 200
    assert "15.0" in response.get_data(as_text=True)


def test_subtraction():
    response = calculate(10, 5, "sub")
    assert response.status_code == 200
    assert "5.0" in response.get_data(as_text=True)


def test_multiplication():
    response = calculate(10, 5, "mul")
    assert response.status_code == 200
    assert "50.0" in response.get_data(as_text=True)


def test_division():
    response = calculate(10, 5, "div")
    assert response.status_code == 200
    assert "2.0" in response.get_data(as_text=True)


def test_division_by_zero():
    response = calculate(10, 0, "div")
    assert response.status_code == 200
    assert "Cannot divide by zero" in response.get_data(as_text=True)


def test_invalid_operation():
    response = calculate(10, 5, "invalid")
    assert response.status_code == 200
    assert "Invalid operation" in response.get_data(as_text=True)
