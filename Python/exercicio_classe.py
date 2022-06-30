class Conta():

    def __init__(self, cpf, nome, saldo):
        self._cpf = cpf
        self._nome = nome
        self._saldo = saldo

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self):
        return self._saldo

    @property
    def setCpf(self,  cpf):
        self._cpf = cpf

    @property
    def setNome(self, nome):
        self._nome = nome

    @property
    def setSaldo(self, Saldo):
        self._Saldo = Saldo

    def depositar(self, deposito):
        self._saldo += deposito

    def sacar(self, saque):
        if saque <= self._saldo:
            self._saldo -= saque
            return saque
        else:
            print(f'saldo insuficiente, saldo atual e: {self._saldo}')

    def toString(self):
        print(f'nome: {self._nome}')
        print(f'cpf: {self._cpf}')
        print(f'saldo: {self._saldo}')


def teste():
    conta_igor = Conta(1, "igor", 10)
    conta_nando = Conta(2, "nando", 100000)
    conta_zig = Conta(3, "zig", 5)
    conta_igor.toString()
    print("\n")
    conta_nando.toString()
    print("\n")
    conta_zig.toString()
    print("\n")
    conta_igor.depositar(100)
    conta_nando.depositar(2000)
    conta_zig.depositar(5)
    conta_igor.toString()
    print("\n")
    conta_nando.toString()
    print("\n")
    conta_zig.toString()


if __name__ == '__main__':
    teste()
