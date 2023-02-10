import pytest
from ..constant import api_base_url

@pytest.mark.update
@pytest.mark.parametrize("my_id, fullname, email, birth, gender, phone, expected_status_code", [
    ("36", "Heghine", "hegh_2@gmail.com", "2004-02-08", "f", "099999999", 200),
])
def test_register(session, my_id, fullname, email, birth, gender, phone, expected_status_code):
    response = session.put(
        f"{api_base_url}users/{my_id}",
        json={"fullname": fullname, "email": email, "birth": birth, "gender": gender, "phone": phone}
    )   
    assert response.status_code == expected_status_code

