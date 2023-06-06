import math

class FiguraGeometrica:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        # Considerando que o triângulo é isósceles (dois lados iguais)
        hipotenusa = math.sqrt((self.base / 2)**2 + self.altura**2)
        return self.base + 2 * hipotenusa

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * (self.raio**2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.raio

# Testando as classes e métodos

retangulo = Retangulo(5, 3)
print("Área do retângulo:", retangulo.calcularArea())
print("Perímetro do retângulo:", retangulo.calcularPerimetro())

triangulo = Triangulo(4, 6)
print("Área do triângulo:", triangulo.calcularArea())
print("Perímetro do triângulo:", triangulo.calcularPerimetro())

circulo = Circulo(2)
print("Área do círculo:", circulo.calcularArea())
print("Circunferência do círculo:", circulo.calcularPerimetro())