dias = int(input("digite os dias:"))

semana = dias // 7
resto_dia = dias % 7

print(f"{dias} são equivalentes á {semana} semanas e {resto_dia:.0f} dias")