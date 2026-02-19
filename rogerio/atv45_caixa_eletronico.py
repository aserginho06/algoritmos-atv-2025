valor = int(input())

n50 = valor // 50

valor = valor - (n50 * 50)

n10 = valor // 10
valor = valor - (n10 * 10)

n5 = valor // 5
valor = valor - (n5 * 5)

n1 = valor

print(n50)
print(n10)
print(n5)
print(n1)