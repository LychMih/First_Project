class Crypt:
    def __init__(self, password, text):
        self.password = password
        self.text = text

    def crypto(self):
        crypt_text: str = ""
        i = 1
        for ch in self.text:
            crypt_text += chr(ord(ch) ^ (255 - ord(self.password[i - 1])))
            if i < len(self.password):
                i += 1
            else:
                i = 1
        return crypt_text

text = input("Enter text...")
password = input("Enter password...")
shifrovanii_text = Crypt(password, text).crypto()
print(shifrovanii_text)
rasshifrovanii_text = Crypt(password, shifrovanii_text).crypto()
print(rasshifrovanii_text)
print(shifrovanii_text)
