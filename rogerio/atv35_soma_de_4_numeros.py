numero = int(input("digite um numero:"))

milhar = (numero //1000) % 10
centena= (numero // 100) % 10
dezena = (numero // 10) % 10
unidade= numero % 10

soma = milhar + centena + dezena + unidade

print(f"a soma dos algarismos desses numeros é {soma}")