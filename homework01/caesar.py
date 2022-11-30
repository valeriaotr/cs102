import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    encrypted = ""
    for symbol in plaintext:
        if symbol.isupper():
            symbol_index = ord(symbol) - ord("A")
            new_symbol = chr((symbol_index + shift) % 26 + ord("A"))
            encrypted += new_symbol
        elif symbol.islower():
            symbol_index = ord(symbol) - ord("a")
            new_symbol = chr((symbol_index + shift) % 26 + ord("a"))
            encrypted += new_symbol
        elif symbol.isdigit():
            encrypted += str(symbol)
        else:
            encrypted += symbol
    return encrypted


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for symbol in ciphertext:
        if symbol.isupper():
            symbol_index = ord(symbol) - ord("A")
            new_symbol = chr((symbol_index - shift) % 26 + ord("A"))
            plaintext += new_symbol
        elif symbol.islower():
            symbol_index = ord(symbol) - ord("a")
            new_symbol = chr((symbol_index - shift) % 26 + ord("a"))
            plaintext += new_symbol
        elif symbol.isdigit():
            plaintext += str(symbol)
        else:
            plaintext += symbol
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:

    """

    Brute force breaking a Caesar cipher.

    """

    best_shift = 0

    # PUT YOUR CODE HERE

    return best_shift