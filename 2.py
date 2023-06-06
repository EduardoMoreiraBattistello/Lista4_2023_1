class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("Acelerando o veículo!")

    def frear(self):
        print("Freando o veículo!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

    def ligar_radio(self):
        print("Ligando o rádio do carro!")

    def abrir_porta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Empinando a moto!")

    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima

    def carregar(self):
        print("Carregando o caminhão!")

    def descarregar(self):
        print("Descarregando o caminhão!")

# Testando as classes e métodos

carro = Carro("Fiat", "Uno", 2018, "Vermelho")
carro.acelerar()
carro.frear()
carro.ligar_radio()
carro.abrir_porta()

moto = Moto("Honda", "CB500", 2020, "500 cc")
moto.acelerar()
moto.frear()
moto.empinar()
moto.buzinar()

caminhao = Caminhao("Volvo", "FH440", 2015, "30 ton")
caminhao.acelerar()
caminhao.frear()
caminhao.carregar()
caminhao.descarregar()