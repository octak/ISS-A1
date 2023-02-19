def rail_fence_cipher_encryption(plaintext: str, key: int = 3):
    ciphertext = ""
    for i in range(0, key):
        ciphertext += plaintext[i::key]
    return ciphertext


def rail_fence_cipher_decryption(ciphertext):
    length = len(ciphertext)

    if length < 4:
        return ciphertext

    third_length = length // 3 + (1 if length % 3 else 0)

    ciphertext_list = list(ciphertext)

    if length % 3 == 1:
        ciphertext_list.insert(third_length * 2 - 1, '')

    plaintext = ''.join(''.join(ciphertext_list[i::third_length]) for i in range(third_length))

    return plaintext


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
