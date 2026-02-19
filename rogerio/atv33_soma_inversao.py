numero = int(input("digite um numero:"))

centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero % 10
invertido = str(unidade) + str(dezena) + str(centena)

soma = numero + int(invertido)

print(f" a soma do numero {numero}  o inverso dele é {soma}")