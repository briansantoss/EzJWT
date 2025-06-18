BASE64URL_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
GROUPS_LEN_BITS = 6

def base64url_encode(input_bytes: bytes) -> str:
    # Convert input bytes to a single binary string
    input_bits = ''.join(f'{byte:08b}' for byte in input_bytes)

    # Split the bit string into 6-bit groups and pad the last group with zeros if necessary
    groups = [input_bits[i: i + GROUPS_LEN_BITS].ljust(GROUPS_LEN_BITS, '0') for i in
              range(0, len(input_bits), GROUPS_LEN_BITS)]
    # Map each 6-bit group to the corresponding Base64URL character
    return ''.join(BASE64URL_TABLE[int(group, 2)] for group in groups)


def base64url_decode(encoded: str) -> bytes:
    input_bits = ''.join(f'{BASE64URL_TABLE.index(char):0{GROUPS_LEN_BITS}b}' for char in encoded)

    # Group bits in 8-bits (bytes) blocks excluding incomplete ones
    blocks = [input_bits[i: i + 8] for i in range(0, len(input_bits) // 8 * 8, 8)]
    return bytes([int(byte, 2) for byte in blocks])