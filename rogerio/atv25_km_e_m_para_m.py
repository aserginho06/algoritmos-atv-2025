km_total = int (input("digite quantos km:"))
metro_total = int (input("digite quantos metros:"))

conversor = (km_total * 1000) + metro_total

print(f"{km_total}Km e {metro_total}m em metros é {conversor:.2f}")