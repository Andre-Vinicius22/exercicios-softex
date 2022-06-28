try:
    loop = True
    nome = input("Digite seu Nome completo: ")
    while loop:
        ano_nascimento = str(input("Digite seu ano de nascimento: "))
        if len(ano_nascimento) == 4 and ano_nascimento.isnumeric:
            ano_nascimento = int(ano_nascimento)
            if (ano_nascimento > 1921) and (ano_nascimento < 2022):
                idade = 2022 - ano_nascimento
                print(
                    f'Ola: {nome}, no ano de 2022 voce possui ou ira completar {idade} anos.')
                loop = False
        else:
            print("insira um ano de nascimento valido")
except Exception as e:
    print("Ocorreu um erro")
    print(e)
