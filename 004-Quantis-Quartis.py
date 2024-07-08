import pandas

df = pandas.read_csv('002-BigmacPriceJuly2022.csv')

# 1st Quartil
print(df['dollar_price'].quantile(0.25))

# 1st and 2nd Quartil
print(df['dollar_price'].quantile(0.50))
print(df['dollar_price'].median())
