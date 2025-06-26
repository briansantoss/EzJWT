from base64url import base64url_encode, base64url_decode
from hs256 import hs256
from json import dumps

def jwt_encode(secret: bytes, payload: dict) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64url_encode(dumps(header, separators=(',',':')).encode())
    payload_b64 = base64url_encode(dumps(payload, separators=(',',':')).encode())

    signature = hs256(secret, header_b64 + b'.' + payload_b64)
    return (header_b64 + b'.' + payload_b64 + b'.'+ base64url_encode(signature)).decode()