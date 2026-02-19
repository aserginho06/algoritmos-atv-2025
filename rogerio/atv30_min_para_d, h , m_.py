min = int(input("digite os minutos:"))

dia = min //1440
semana = dia // 7
horas = min // 60
print(f"{min} minutos são equivalentes á {semana} semanas, {dia} dias e {horas} horas")