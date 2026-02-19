numero = int(input("digite um numero:"))

centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero %10

soma_dois = centena + dezena
subtrai_dois = dezena - unidade

print(f"a soma dos dois primeiros algarismos de {numero} é {soma_dois} e e a diferença dos dois ultimos é {subtrai_dois}")