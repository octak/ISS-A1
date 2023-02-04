import socket

import part_1_encryption_algorithms as encryption


def encrypt_file_contents(filename: str = "NoMoreMurders.dat") -> str:
    try:
        with open(filename, "r") as file:
            return encryption.encryption(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


def write_encrypted_contents_to_file(encrypted_contents: str, filename: str = "RowleyA.dat"):
    with open(filename, "w") as file:
        file.write(encrypted_contents)


def send_file_to_program_b(filename: str = "RowleyA.dat"):
    try:
        with open(filename, "rb") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 44444))

    # sends the file size in bytes
    client.send(str(len(contents)).zfill(10).encode())

    # sends the file contents
    client.sendall(contents)

    client.close()


if __name__ == '__main__':
    write_encrypted_contents_to_file(encrypt_file_contents())
    send_file_to_program_b()
