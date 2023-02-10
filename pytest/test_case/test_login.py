import pytest

@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_status_code", [
    ("heghine.sarkisyan.im@gmail.com", "hi", 200),
    ("avo_1@gmail.com", "hi", 200),
    ("arman_1@gmail.com", "hi", 200),
])
def test_login(api_base_url, session, username, password, expected_status_code):
    response = session.post(
        f"https://demoapp-testing.herokuapp.com/users/login",
        data={"username": username, "password": password}
    )
    assert response.status_code == expected_status_code


