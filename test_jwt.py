import pytest
from jwt import jwt_encode

test_cases = [
    (b'a-string-secret-at-least-256-bits-long', {
        "sub": "1234567890",
        "name": "John Doe",
        "admin": True,
        "iat": 1516239022
    },
     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
     'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.'
     'KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30'),
]

@pytest.mark.parametrize('secret, payload, expected', test_cases)
def test_jwt_encode(secret, payload, expected):
    jwt = jwt_encode(secret, payload)
    assert jwt == expected