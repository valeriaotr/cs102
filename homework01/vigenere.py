def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    i = len(keyword)
    for symbol in plaintext:
        if len(keyword) < i + 1:
            i = 0
        if symbol.isupper():
            symbol_index = ord(symbol) - ord("A")
            new_symbol = chr((symbol_index + (ord(keyword[i]) - ord("A"))) % 26 + ord("A"))
            ciphertext += new_symbol
        elif symbol.islower():
            symbol_index = ord(symbol) - ord("a")
            new_symbol = chr((symbol_index + (ord(keyword[i]) - ord("a"))) % 26 + ord("a"))
            ciphertext += new_symbol
        elif symbol.isdigit():
            ciphertext += str(symbol)
        else:
            ciphertext += symbol

        i += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    i = len(keyword)
    for symbol in ciphertext:
        if len(keyword) < i + 1:
            i = 0
        if symbol.isupper():
            symbol_index = ord(symbol) - ord("A")
            new_symbol = chr((symbol_index - (ord(keyword[i]) - ord("A"))) % 26 + ord("A"))
            plaintext += new_symbol
        elif symbol.islower():
            symbol_index = ord(symbol) - ord("a")
            new_symbol = chr((symbol_index - (ord(keyword[i]) - ord("a"))) % 26 + ord("a"))
            plaintext += new_symbol
        elif symbol.isdigit():
            plaintext += str(symbol)
        else:
            plaintext += symbol
        i += 1
    return plaintext
