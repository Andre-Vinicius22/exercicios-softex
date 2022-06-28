from enum import Enum
class Candidatos(Enum):
    CANDIDATO_X = 889
    CANDIDATO_Y = 847
    CANDIDATO_Z = 515
    BRANCO = 0

def start():
    opcao = criacao_opcao_dic()
    loop = True
    while loop:
        menu()
        voto = valida_input()
        contagem_votos(opcao, voto)
        loop = continua_loop()
    mostrar_resultado(opcao)

def criacao_opcao_dic():
    opcao = {'candidato_x': 0, 'candidato_y': 0, 'candidato_z': 0,  'branco' : 0,  'nulo': 0}
    return opcao

def menu():
    print("------------Eleição------------")
    print(" 889 - para votar no cadidato X")
    print(" 847 - para votar no cadidato Y")
    print(" 515 - para votar no cadidato Z")
    print(" 0   - para votar em Branco.   ")
    print("--------------------------------")

def valida_input():
    escolha = input("Digite seu voto: ")
    if escolha.isnumeric():
        return int(escolha)
    else:
        return 'voto'

def contagem_votos(opcao, voto):
    if voto == Candidatos.CANDIDATO_X.value:
        opcao['candidato_x'] = opcao['candidato_x']+ 1
    elif voto == Candidatos.CANDIDATO_Y.value:
        opcao['candidato_y'] = opcao['candidato_y']+ 1
    elif voto == Candidatos.CANDIDATO_Z.value:
        opcao['candidato_z'] = opcao['candidato_z']+ 1
    elif voto == Candidatos.BRANCO.value:
        opcao['branco'] = opcao['branco']+ 1
    elif str(voto).isalpha():
        print("opcao invalida, caracteres nao sao permitidos")
    else:
        opcao['nulo'] = opcao['nulo']+ 1

def continua_loop():
    escolha = input("Deseja continuar votando? ").lower().strip()
    if escolha == 's':
        return True
    else:
        return False

def mostrar_resultado(opcao):
    print(opcao)

if __name__ == '__main__':
    start()