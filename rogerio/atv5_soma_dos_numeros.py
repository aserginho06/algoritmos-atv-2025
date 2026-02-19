numero = int(input("digite um numero:"))

centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero %10

soma_de_todos = centena + dezena + unidade

print(f"a soma de todos os algarismos de {numero} é {soma_de_todos}")