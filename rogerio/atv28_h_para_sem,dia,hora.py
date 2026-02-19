hora = int(input("digite os seg:"))

dia =  hora // 24
semana = dia // 7
horas = hora % 24
print(f"{hora} horas são equivalentes á {semana} semanas e {dia} dias e {horas:.0f} horas")