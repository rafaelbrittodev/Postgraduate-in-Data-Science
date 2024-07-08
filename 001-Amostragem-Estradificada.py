import pandas
from random import sample

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = ["A", "A", "A", "A", "B", "B", "C", "C", "C", "D", "D", "D"]

df = pandas.DataFrame({"grupo": b, "values": a})

df

# Amostragem Estradificada = Metódo de amostragem que analisa uma população à dividindo em subpopulações


# Amostra aleatória em cada estrato por grupo
def amostra_estradificada_1(df, n, extrato):
    amostra = df.groupby(extrato, group_keys=False).apply(
        lambda x: x.sample(min(len(x), n)))

    return amostra


# Amostra por taxa de representatividade de cada grupo
def amostra_estradificada_2(df, n, extrato):
    tamanho_pop = df.shape[0]
    amostra = df.groupby(extrato, group_keys=False)\
        .apply(lambda x: x.sample(int(n*len(x)/tamanho_pop)))\
        .reset_index(drop=True)\
        .sort_values(by=extrato)

    return amostra


# Amostra por conglomerado
def amostra_conglomerado(df, n_conglomerado, conglomerado):
    todos_conglomerados = list(df[conglomerado].unique())
    tamanho_conglomerados = len(todos_conglomerados)
    n = min(n_conglomerado, tamanho_conglomerados)
    conglomerado_sorteados = sample(todos_conglomerados, n)

    amostra = df[df[conglomerado].isin(conglomerado_sorteados)]
    return amostra


print(amostra_estradificada_1(df, 1, 'grupo'))

print(amostra_estradificada_2(df, 6, 'grupo'))

print(amostra_conglomerado(df, 2, 'grupo'))
