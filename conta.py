class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_extrato(self):
        return "o saldo em conta é de R${}".format(self.__saldo)

    def get_titular(self):
        return self.__titular

    def depositar(self, valor_deposito):
        self.__saldo += valor_deposito

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor_saque):
        if(self.__pode_sacar(valor_saque)):
            self.__saldo -= valor_saque
        else:
            print("saldo insuficiente")

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"
