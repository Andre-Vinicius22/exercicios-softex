# funções para as operações.
def soma(num1, num2):
    print(num1 + num2)


def subtrai(num1, num2):
    print(num1 - num2)


def multiplica(num1, num2):
    print(num1 * num2)


def divide(num1, num2):
    if num2 == 0:
        return print("0 nao e um dividendo!!")
    print(num1 / num2)

# função calculadora!


def Calculadora(num1, num2, opr):
    if opr == 1:
        soma(num1, num2)
    elif opr == 2:
        subtrai(num1, num2)
    elif opr == 3:
        multiplica(num1, num2)
    elif opr == 4:
        divide(num1, num2)
    else:
        print("resultado = 0, operação inexistente")


Calculadora(1, 2, 1)  # soma
Calculadora(4, 3, 2)  # subtrai
Calculadora(5, 5, 3)  # multiplica
Calculadora(12, 2, 4)  # divide
