import socket

import encryption_algorithms as encryption


def receive_file_from_program_a(filename: str = "RowleyB.dat"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 44444))
    server.listen()

    while True:
        client, addr = server.accept()

        # receives the file size from the client, decodes it, and strips the leading zeroes
        size = int(client.recv(10).decode().strip())

        # receives the file contents from the client
        contents = client.recv(size)

        server.close()
        break

    with open(filename, "wb") as file:
        file.write(contents)


def brute_force_decryption(filename="RowleyB.dat", keyfile="keywords.dat"):
    """
    Assuming prior knowledge of the encryption algorithms used, the program will generate random keys for the caesar
    and rail fence ciphers, until words fromm the list of keywords are detected in the output of the decryption.

    Specifications
    1. The caesar cipher has keys from 1 to n, where n is the number of available characters in the character set. Here,
       that value is 127.
    2. The rail fence cipher's key goes from 2 to n, where n is the number of characters in the plaintext.
    """

    try:
        with open(filename, 'r') as file:
            contents = file.read()
            if not contents:
                print(f"Error: The file '{filename}' is empty. Program B will not attempt to decrypt it.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Program B will not attempt to decrypt it.")
        return

    try:
        with open(keyfile, 'r') as file:
            keywords = file.read().splitlines()
    except FileNotFoundError:
        print(f"Warning: The file '{keyfile}' does not exist. Using built-in keywords.")
        keywords = ["crime", "murder", "violence", "safety", "criminal", "criminals", "dear", "prime", "minister",
                    "country", "killing", "killed", "killed", "killed", "unfair", "injustice", "justice", "afraid",
                    "fear", "guns", "law", "lawlessness", "rate", "murder", "murderer", "police", "policing", "budget",
                    "corruption", "money", "thieves", "gangs", "gang", "increasing", "decreasing", "since"]

    found_keywords = []
    for caesar_key in range(1, 127):
        for rail_fence_key in range(2, len(contents) - 1):
            decrypted_contents = encryption.decryption(contents, rail_fence_key=3, caesar_key=caesar_key)
            for keyword in keywords:
                if keyword in decrypted_contents:
                    found_keywords.append(keyword)
            if found_keywords:
                print(f"The algorithm has detected the following keywords in the decrypted text: {found_keywords}.")
                print(f"The rail fence cipher key is {rail_fence_key} and the caesar cipher key is {caesar_key}.")
                print("The decrypted message is below.\n")
                print(decrypted_contents)
            break
        break


if __name__ == '__main__':
    receive_file_from_program_a()
    brute_force_decryption()
