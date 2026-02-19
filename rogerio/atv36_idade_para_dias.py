idadeano = int(input("digite o ano:"))
idademes = int(input("digite os meses:"))
idadedia = int(input("digite os dias"))

dias = (idadeano * 365.25) + (idademes * 30) + idadedia 
# 365.25 para anos bissextos

print(f'a quantidade de dias que essa pessoa está viva é {dias:.0f}')