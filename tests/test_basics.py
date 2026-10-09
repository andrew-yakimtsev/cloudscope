def is_successful_response(status_code: int) -> bool:
    return 200 <= status_code <= 299

def test_successful_response():
    assert is_successful_response(200) == True
    assert is_successful_response(201) == True
    assert is_successful_response(204) == True
    assert is_successful_response(299) == True

    assert is_successful_response(199) == False
    assert is_successful_response(300) == False
    assert is_successful_response(404) == False
    assert is_successful_response(500) == False