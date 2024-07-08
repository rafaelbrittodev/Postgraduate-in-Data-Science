import pandas

# df = pandas.read_csv('002-BigmacPrice.csv')

# # print(df.head())
# # print(df.dtypes)

# # Criando filtro por data
# df_filtered = df[df['date'] == '2022-07-01']

# print(df_filtered.head())
# print(df_filtered.count())
# print(df_filtered.groupby('name').count()['date'])

# df_filtered.to_csv('002-BigmacPriceJuly2022.csv', index=False)



# MODA = Valor que mais se repete
df = pandas.read_csv('002-BigmacPriceJuly2022.csv')

print(df['dollar_price'].mode())

# MEDIA = Aritimética simples de todos os valores
print(df['dollar_price'].mean())

# MEDIANA = Encontra o dado central da amostragem
print(df['dollar_price'].median())