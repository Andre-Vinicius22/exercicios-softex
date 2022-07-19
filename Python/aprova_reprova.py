aluno = "Maria"
nota1 = 3
nota2 = 3
res_media = nota1 + nota2 / 2
faltas = 1

if res_media < 7:
    print(aluno + " Reprovado(a) por nao atingir a media ")

aluno = "Joao"
nota1 = 9
nota2 = 10
faltas = 5

if faltas > 3:
    print(aluno + " Reprovado(a) por exceder o numero de faltas ")

aluno = "Pedro"
nota1 = 10
nota2 = 9
res_media = nota1 + nota2

if res_media >= 7:
    print(aluno + " Aprovado(a) ")
