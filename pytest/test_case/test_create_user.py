import pytest

@pytest.mark.create_user
@pytest.mark.parametrize("fullname, email, birth, gender, phone, password, expected_status_code", [
    ("Heghine", "hegh_2@gmail.com", "2004-02-08", "f", "099999999", "hi", 409),
    ("Avo", "avo_2@gmail.com", "1999-09-29", "g", "099999999", "hi", 409),
    ("Arman", "arman_2@gmail.com", "2000-02-08", "g", "099999999", "hi", 409),
])
def test_register(api_base_url, session, fullname, email, birth, gender, phone, password, expected_status_code):
    response = session.post(
        f"https://demoapp-testing.herokuapp.com/users/",
        json={"fullname": fullname, "email": email, "birth": birth, "gender": gender, "phone": phone, "password": password}
    )
    assert response.status_code == expected_status_code

