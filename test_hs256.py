import pytest
from hs256 import hs256
import hashlib, hmac

test_cases = [
    (b'\x0b' * 20, b'Hi There', hmac.new(b'\x0b' * 20, b'Hi There', hashlib.sha256).digest()),
    (b'Jefe', b'what do ya want for nothing?', hmac.new(b'Jefe', b'what do ya want for nothing?', hashlib.sha256).digest()),
    (b'\xaa' * 20, b'\xdd' * 50, hmac.new(b'\xaa' * 20, b'\xdd' * 50, hashlib.sha256).digest()),
    (bytes(range(1, 26)), b'\xcd' * 50, hmac.new(bytes(range(1, 26)), b'\xcd' * 50, hashlib.sha256).digest()),
]

@pytest.mark.parametrize('key, message, expected', test_cases)
def test_hmac(key, message, expected):
    h = hs256(key, message)
    assert h == expected, f'Expected {expected} but got {h}'

