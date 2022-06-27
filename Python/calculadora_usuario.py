def soma(num1, num2):
    resultado = num1 + num2
    print(f'Resultado da soma = {resultado}')


def subtrai(num1, num2):
    resultado = num1 - num2
    print(f'Resultado da subtracao = {resultado}')


def multiplica(num1, num2):
    resultado = num1 * num2
    print(f'Resultado da multiplicacao = {resultado}')


def divide(num1, num2):
    resultado = num1 / num2
    print(f'Resultado da divisao = {resultado}')


def menu():
    print("-----Calculadora-----")
    print("|  1 - somar        |")
    print("|  2 - subtrair     |")
    print("|  3 - multiplicar  |")
    print("|  4 - dividir      |")
    print("|  0 - Sair         |")
    print("---------------------")


def Calculadora():

    while True:
        menu()
        escolha = entrada_usuario()
        if escolha == 1:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            soma(num1, num2)

        elif escolha == 2:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            subtrai(num1, num2)

        elif escolha == 3:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            multiplica(num1, num2)

        elif escolha == 4:
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            divide(num1, num2)

        elif escolha == 0:
            return
        else:
            print("--------------------------")
            print("!!!OPERACAO INEXISTENTE!!!")
            print("--------------------------")


def entrada_usuario():
    return int(input("Escolha um numero: "))


if __name__ == '__main__':
    Calculadora()
