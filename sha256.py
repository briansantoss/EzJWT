BIT_MASK = 0xFFFFFFFF

def sha256_hash(input_bytes: bytes) -> bytes:
    # Define constantes importantes
    blocks_size_bits = 512
    words_per_block = 16
    words_size_bits = 32

    # Convert input_bytes to a single binary string
    input_bytes = ''.join(f'{byte:08b}' for byte in input_bytes)

    # Obtém o tamanho da entrada original (em bits)
    input_bits_size = len(input_bytes)

    # Calcula a quantidade de preenchimento necessária
    pad_quant = (448 - (len(input_bytes) + 1) % blocks_size_bits) % blocks_size_bits

    # Adiciona o bit 1 (como "string") à entrada
    input_bytes += '1'

    # Aplica o preenchimento
    input_bytes += pad_quant * '0'

    # Coloca o tamanho da entrada original (em bits) nos últimos 64 bits da mensagem original já preenchida
    input_bytes += f'{input_bits_size:064b}'

    # Gera os blocos de 512 bits
    blocks = [input_bytes[i:i + blocks_size_bits] for i in range(0, len(input_bytes), blocks_size_bits)]

    # Gera as 16 palavras de 32 bits para cada bloco
    blocks = [[int(block[i:i +  words_size_bits], 2) for i in range(0, blocks_size_bits, words_size_bits)] for block in blocks]

    # Expande para as 64 palavras
    for block in blocks:
        for i in range(16, 64):
            # Gera uma nova palavra de 32 bits
            new_word = (lsigma1(block[i - 2]) + block[i - 7] + lsigma0(block[i - 15]) + block[i - 16]) & BIT_MASK
            block.append(new_word)

    # Inicializando os 8 registradores
    registers = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    # Definindo as 64 constantes
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    for block in blocks:
        # Inicializa as variáveis de trabalho
        a, b, c, d, e, f, g, h = registers[:]
        for i in range(64):
            temp1 = (h + usigma1(e) + choice(e, f, g) + K[i] + block[i]) & BIT_MASK
            temp2 = (usigma0(a) + majority(a, b, c)) & BIT_MASK

            # Atualizando as variáveis
            h = g
            g = f
            f = e
            e = (d + temp1) & BIT_MASK
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & BIT_MASK

        # Atualizando os registradores
        registers[0] = (registers[0] + a) & BIT_MASK
        registers[1] = (registers[1] + b) & BIT_MASK
        registers[2] = (registers[2] + c) & BIT_MASK
        registers[3] = (registers[3] + d) & BIT_MASK
        registers[4] = (registers[4] + e) & BIT_MASK
        registers[5] = (registers[5] + f) & BIT_MASK
        registers[6] = (registers[6] + g) & BIT_MASK
        registers[7] = (registers[7] + h) & BIT_MASK

    return b''.join(hash_value.to_bytes(4, 'big') for hash_value in registers)

def rotr(n:int, word:int):
    return ((word >> n) | (word << (32 - n))) & BIT_MASK

def shr(n:int, word:int) -> int:
    return (word >> n) & 0xFFFFFFFF

def lsigma0(word:int) -> int:
    return rotr(7, word) ^ rotr(18, word) ^ shr(3, word)

def lsigma1(word: int) -> int:
    return rotr(17, word) ^ rotr(19, word) ^ shr(10, word)

def usigma0(word:int) -> int:
    return rotr(2, word) ^ rotr(13, word) ^ rotr(22, word)

def usigma1(word:int) -> int:
    return rotr(6, word) ^ rotr(11, word) ^ rotr(25, word)

def choice(x:int, y:int, z:int) -> int:
    return (x & y) ^ (~x & z)

def majority(x:int, y:int, z:int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)