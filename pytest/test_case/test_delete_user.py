import pytest
from ..constant import api_base_url

@pytest.mark.delete
@pytest.mark.parametrize("id_my, expected_status_code", [
	(32, 204),
	(33, 204),
	(255, 404),
])
def test_login(session, id_my, expected_status_code):
    response = session.delete(
        f"{api_base_url}users/users/{id_my}",
    )   
    assert response.status_code == expected_status_code
