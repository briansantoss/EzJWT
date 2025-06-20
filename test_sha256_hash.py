import pytest
from sha256 import sha256_hash
from hashlib import sha256

test_cases = [
    (b'', sha256(b'').digest()),
    (b'abc', sha256(b'abc').digest()),
    (b'a' * 1000, sha256(b'a' * 1000).digest()),
    (b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq', sha256(b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq').digest()),
]

@pytest.mark.parametrize('input_bytes, expected_digest', test_cases)
def test_sha256_hash(input_bytes: bytes, expected_digest: bytes):
    digest = sha256_hash(input_bytes)
    assert digest == expected_digest, f'Expected {expected_digest} but got {digest}'
