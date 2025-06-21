import pytest
from base64url import base64url_encode, base64url_decode
from base64 import urlsafe_b64encode, urlsafe_b64decode

test_cases = [
    (b'', urlsafe_b64encode(b'').rstrip(b'=')),
    (b'f', urlsafe_b64encode(b'f').rstrip(b'=')),
    (b'fo', urlsafe_b64encode(b'fo').rstrip(b'=')),
    (b'foo', urlsafe_b64encode(b'foo').rstrip(b'=')),
    (b'foob', urlsafe_b64encode(b'foob').rstrip(b'=')),
    (b'fooba', urlsafe_b64encode(b'fooba').rstrip(b'=')),
    (b'foobar', urlsafe_b64encode(b'foobar').rstrip(b'=')),
    (b'any carnal pleasure.', urlsafe_b64encode(b'any carnal pleasure.').rstrip(b'=')),
]

@pytest.mark.parametrize('inpt, expected', test_cases)
def test_encode(inpt, expected):
    encoded = base64url_encode(inpt)
    assert encoded == expected, f'Expected {expected}, got {encoded}'


@pytest.mark.parametrize('expected, inpt', test_cases)
def test_decode(expected, inpt):
    decoded = base64url_decode(inpt)
    assert decoded == expected, f'Expected {expected}, got {decoded}'