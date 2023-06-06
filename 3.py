class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                ascii_code = ord(char)
                ascii_code = (ascii_code - 65 + self.deslocamento) % 26 + 65
                texto_cifrado += chr(ascii_code)
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_original = ""
        for char in texto_cifrado:
            if char.isalpha():
                ascii_code = ord(char)
                ascii_code = (ascii_code - 65 - self.deslocamento) % 26 + 65
                texto_original += chr(ascii_code)
            else:
                texto_original += char
        return texto_original

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for i, char in enumerate(texto):
            ascii_code = ord(char)
            ascii_code ^= ord(self.chave[i % len(self.chave)])
            texto_cifrado += chr(ascii_code)
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_original = ""
        for i, char in enumerate(texto_cifrado):
            ascii_code = ord(char)
            ascii_code ^= ord(self.chave[i % len(self.chave)])
            texto_original += chr(ascii_code)
        return texto_original

# Testando as classes e métodos

cifra_cesar = CifraCesar(3)
texto = "OLA MUNDO"
texto_cifrado = cifra_cesar.cifrar(texto)
texto_decifrado = cifra_cesar.decifrar(texto_cifrado)
print("Texto cifrado (Cifra de César):", texto_cifrado)
print("Texto decifrado (Cifra de César):", texto_decifrado)

cifra_xor = CifraXor("chave123")
texto = "OLA MUNDO"
texto_cifrado = cifra_xor.cifrar(texto)
texto_decifrado = cifra_xor.decifrar(texto_cifrado)
print("Texto cifrado (Cifra XOR):", texto_cifrado)
print("Texto decifrado (Cifra XOR):", texto_decifrado)