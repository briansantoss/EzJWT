from sha256 import sha256_hash
from base64url import base64url_encode, base64url_decode

def hs256(key: bytes, message: bytes) -> bytes:
    hash_block_size = 64
    key_len = len(key)

    if key_len > hash_block_size:
        key = sha256_hash(key)
    elif key_len < hash_block_size:
        key += b'\x00' * (hash_block_size - key_len)

    ipad = b'\x36' * hash_block_size
    opad = b'\x5c' * hash_block_size

    inner = sha256_hash(xor(key, ipad) + message)
    return sha256_hash(xor(key, opad) + inner)

def xor(x: bytes, y: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(x, y))