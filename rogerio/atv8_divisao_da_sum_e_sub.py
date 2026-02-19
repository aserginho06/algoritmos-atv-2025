numero = int(input("digite um numero:"))

dezena = (numero // 10) % 10
unidade = numero %10

soma_dois = dezena + unidade
subtrai_dois = dezena - unidade
divide = soma_dois / subtrai_dois

print(f"a divisão da soma e subtração dos numeros de {numero} é: {divide:.2f}")