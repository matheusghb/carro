class Carro:
    def __init__ (self, ano, marca, modelo, cor, lig):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.lig = lig
        
    def ligar (self, lig):
        if (self.lig == 0):
            self.lig = self.lig + 1
            return print ("Seu carro está ligado. ")
        else:
            return print ("Seu carro já está ligado. ")
            
    def desligar (self,lig):
        if (self.lig == 1):
            self.lig = self.lig - 1
            return print ("Seu carro foi desligado. ")
        else:
            return print ("Seu carro já está desligado. ")
            
    def info (self, ano, marca, modelo, cor):
        return print ("As informações do carro são as seguintes: Seu ano é ", self.ano,', sua marca é ', self.marca,', seu modelo é ', self.modelo, ', e sua cor é ', self.cor, '')

an = int(input("Diga o ano de lançamento de seu carro: "))
ma = input("Diga a marca de seu carro: ")
mo = input ("Diga o modelo de seu carro: ")
co = input ("Diga a cor de seu carro: ")
lig = 0

ca = Carro (an, ma, mo, co, lig)

alt = ''

while (alt != 's'):
    alt = input('Escolha entre revisar as informações - i - desligar o carro - de - ligar o carro - li - ou sair da tela - s - ')
    if (alt == 'i'):
        print (ca.info(an, ma, mo, co))
    elif (alt == 'de'):
        print (ca.desligar(lig))
    elif (alt == 'li'):
        print (ca.ligar(lig))
    elif (alt == 's'):
        print ("Fechando programa. ")
    else:
        print ("Caractére incorreto. ")