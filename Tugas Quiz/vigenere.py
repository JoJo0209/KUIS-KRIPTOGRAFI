class Vigenere:
    @staticmethod
    def encrypt(text, key):
        result = []
        key_length = len(key)
        key_index = 0

        for char in text:
            if char.isalpha():
                base = 'A' if char.isupper() else 'a'
                result_char = chr((ord(char) + (ord(key[key_index].upper()) - ord('A'))) % 26 + ord(base))
                result.append(result_char)
                key_index = (key_index + 1) % key_length
            else:
                result.append(char)

        return ''.join(result)

    @staticmethod
    def decrypt(text, key):
        result = []
        key_length = len(key)
        key_index = 0

        for char in text:
            if char.isalpha():
                base = 'A' if char.isupper() else 'a'
                result_char = chr((ord(char) - (ord(key[key_index].upper()) - ord('A')) + 26) % 26 + ord(base))
                result.append(result_char)
                key_index = (key_index + 1) % key_length
            else:
                result.append(char)

        return ''.join(result)
