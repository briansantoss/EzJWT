import pytest
from hs256 import hs256

test_cases = [
    (b'\x0b' * 20, b'Hi There', 'b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7'),
    (b'Jefe', b'what do ya want for nothing?', '5bdcc146bf60754e6a042426089575c75a003f089d2739839dec58b964ec3843'),
    (b'\xaa' * 20, b'\xdd' * 50, '773ea91e36800e46854db8ebd09181a72959098b3ef8c122d9635514ced565fe'),
    (bytes(range(1, 26)), b'\xcd' * 50,  '82558a389a443c0ea4cc819899f2083a85f0faa3e578f8077a2e3ff46729665b'),
]

@pytest.mark.parametrize('key, message, expected_hex', test_cases)
def test_hmac(key, message, expected_hex):
    h = hs256(key, message)
    assert h.hex() == expected_hex, f'Expected {expected_hex} but got {h}'

