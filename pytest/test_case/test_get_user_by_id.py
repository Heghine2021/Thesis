import pytest

@pytest.mark.get_user_by_id
@pytest.mark.parametrize("id_my, expected_status_code", [
    (19, 404),
    (232, 200),
    (238, 200),
])
def test_login(api_base_url, session, id_my, expected_status_code):
    response = session.get(
        f"https://demoapp-testing.herokuapp.com/users/{id_my}",
    )
    assert response.status_code == expected_status_code

