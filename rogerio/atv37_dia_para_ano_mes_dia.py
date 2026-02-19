idadedia = int(input("digite os dias"))

idadeano = idadedia // 365.25
dias_restantes = idadedia % 365.25
# 365.25 para anos bissextos
idademes = dias_restantes // 30
diaidade =  dias_restantes % 30

print(f' se a pessoa está viva á {idadedia:.0f} dias, então ela tem {idadeano:.0f} anos, {idademes:.0f} meses e {diaidade:.0f} dias ')