class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero__ = numero
        self.__titular__ = titular
        self.__saldo__ = saldo
        self.__limite__ = limite

    def obter_saldo(self):
        return "o saldo em conta é de R${}".format(self.__saldo__)

    def depositar(self, valor_deposito):
        self.__saldo__ += valor_deposito

    def sacar(self, valor_saque):
        self.__saldo__ -= valor_saque

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)