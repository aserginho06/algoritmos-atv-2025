seg = int(input("digite os seg:"))

horas = seg // 60 // 60
min = seg // 60
seg_2 =  seg % 60

print(f"{seg} são equivalentes á {horas} horas e {min} minutos e {seg_2:.0f} segundos")