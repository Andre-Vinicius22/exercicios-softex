class Funcionario():
    def __init__(self, nome, idade):
        self._nome = nome
        if idade >= 1 and idade < 100:
            self._idade = idade
        else:
            print(f'Funcionario {self._nome} informou uma idade invalida!')

    @property
    def getNome(self):
        return self._nome

    def setIdade(self, idade):
        self._idade = idade

    @property
    def getIdade(self):
        return self._idade

funcionario_1 = Funcionario("andre", 22)
print(funcionario_1.getNome)
print(funcionario_1.getIdade)

funcionario_2 = Funcionario("vinicius", 22)
funcionario_2.setIdade(23)
print(funcionario_2.getNome)
print(funcionario_2.getIdade)
