import pandas
import numpy as np

df = pandas.read_csv('002-BigmacPriceJuly2022.csv')
lista_exemplo_variancia = [1, 2, 3, 4, 5]


# Variância = Média do quadrado de distância entre cada observação e a média
def media(lista):
    return sum(lista)/len(lista)


def variancia_amostral(lista):
    media_lista = media(lista)
    tamanho_lista = len(lista)

    lista_distancia_quadradas = []
    for observacao in lista:
        distancia_quadrada = (observacao - media_lista) ** 2
        lista_distancia_quadradas.append(distancia_quadrada)

    variancia = sum(lista_distancia_quadradas) / (tamanho_lista - 1)

    return variancia


def variancia_populacional(lista):
    media_lista = media(lista)
    tamanho_lista = len(lista)

    lista_distancia_quadradas = []
    for observacao in lista:
        distancia_quadrada = (observacao - media_lista) ** 2
        lista_distancia_quadradas.append(distancia_quadrada)

    variancia = sum(lista_distancia_quadradas) / tamanho_lista

    return variancia


print(variancia_populacional(lista_exemplo_variancia))
print(np.var(lista_exemplo_variancia))

print(df['dollar_price'].var())

# Desvio Padrão = Raiz quadrada da variância
print(df['dollar_price'].std())

# Coeficiente de Variação = Nível de variabilidade dentro da população
coeficiente_variacao_big_mac = 100 * df['dollar_price'].std()/df['dollar_price'].mean()
print(coeficiente_variacao_big_mac)