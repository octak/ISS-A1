from collections import Counter


def attempt_frequency_analysis(filename="Rowley.dat"):
    try:
        with open(filename, 'r') as file:
            ciphertext = file.read()
            if not ciphertext:
                print(f"Error: The file '{filename}' is empty.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return

    # print(ciphertext)
    # print(Counter(ciphertext))

    # make all letters uppercase
    ciphertext = uppercase(ciphertext)

    # get most common characters in the ciphertext, assuming alphabet and spaces
    ciphertext_character_frequencies = Counter(ciphertext).most_common(27)

    # english alphabet sorted by frequency
    letter_frequencies = {'E': 0.1202, 'T': 0.091, 'A': 0.0812, 'O': 0.0768, 'I': 0.0731, 'N': 0.0695,
                          'S': 0.0628, 'R': 0.0602, 'H': 0.0592, 'D': 0.0432, 'L': 0.0398, 'U': 0.0288,
                          'C': 0.0271, 'M': 0.0261, 'F': 0.023, 'Y': 0.0211, 'W': 0.0209, 'G': 0.0203,
                          'P': 0.0182, 'B': 0.0149, 'V': 0.0111, 'K': 0.0069, 'X': 0.0017, 'Q': 0.0011,
                          'J': 0.001, 'Z': 0.0007}

    # because ciphertext contains at least 1000 words, the space is probably the most common character
    english_character_frequencies = list(letter_frequencies.items())
    english_character_frequencies.insert(0, (' ', 0.2001))

    print(ciphertext_character_frequencies)
    print(english_character_frequencies)

    # plaintext = ""
    # for character in ciphertext:
    #     index = get_frequency_index(character, ciphertext_character_frequencies)
    #     if index != None:
    #         # print(f"Ciphertext: '{character}' | Index: {index} | Plaintext: {english_character_frequencies[index][0]}")
    #         plaintext += english_character_frequencies[index][0]
    #     else:
    #         plaintext += character
    #
    # print(plaintext)


def get_frequency_index(character: str, ciphertext_character_frequencies: list):
    # find position of tuple representing character and frequency
    for _, tuple in enumerate(ciphertext_character_frequencies):
        if character == tuple[0]:
            return _
    return None


def uppercase(string):
    return ''.join([char.upper() if char.isalpha() else char for char in string])


if __name__ == '__main__':
    attempt_frequency_analysis()
