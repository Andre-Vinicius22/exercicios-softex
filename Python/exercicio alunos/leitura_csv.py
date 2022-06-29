import pandas as pd

df = pd.read_csv('notas_alunos.csv')

media = df["nota_1"] + df["nota_2"]
media = media / 2
df["media"] = media

situacao = " "
df["situacao"] = situacao
df.loc[df["media"] >= 7, "situacao"] = "APROVADO"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO"


df.to_csv('alunos_situacao.csv')

maior_numero_faltas = df["faltas"].max()
print("Maior numero de faltas: " + str(maior_numero_faltas))

media_geral = df["media"].median()
print("A media geral da turma foi: " + str(media_geral))

maior_media = df["media"].max()
print("A maior media da turma foi: " + str(maior_media))