# Rail cipher with key of 3
def rail_fence_cipher_encryption(plaintext: str, key: int = 3):
    ciphertext = ""
    for i in range(0, key):
        ciphertext += plaintext[i::key]
    return ciphertext


# IMPORTANT - REWRITE THE CODE BELOW !!!
# IMPORTANT - REWRITE THE CODE BELOW !!!
# IMPORTANT - REWRITE THE CODE BELOW !!!
def rail_fence_cipher_decryption(cypher):
    length = len(cypher)
    if length < 4: return cypher
    third = length // 3 + (1 if length % 3 else 0)
    cypher = list(cypher)
    if length % 3 == 1: cypher.insert(third * 2 - 1, '')
    return ''.join(''.join(cypher[i::third]) for i in range(third))


# IMPORTANT - REWRITE THE CODE ABOVE !!!
# IMPORTANT - REWRITE THE CODE ABOVE !!!
# IMPORTANT - REWRITE THE CODE ABOVE !!!


def caesar_cipher_encryption(plaintext: str, key: int = 1):
    if all(ord(character) in range(0, 126) for character in plaintext):
        return "".join([chr(ord(character) + key % 126) for character in plaintext])
    return None


def caesar_cipher_decryption(ciphertext: str, key: int = 1):
    if all(ord(character) in range(0, 126) for character in ciphertext):
        return "".join([chr(ord(character) - key % 126) for character in ciphertext])
    return None


def encryption(plaintext: str):
    return caesar_cipher_encryption(rail_fence_cipher_encryption(plaintext))


def decryption(ciphertext: str, rail_fence_key: int = 3, caesar_key: int = 1):
    return rail_fence_cipher_decryption(caesar_cipher_decryption(ciphertext, caesar_key))


if __name__ == '__main__':
    enc = encryption("Iliaj flarsentoj kaj audado estas multmaniere superaj ol tiuj de homoj!")
    print(decryption(enc))
