anos = int(input())
cigarros_dia = int(input())
preco_carteira = float(input())

total_cigarros = anos * 365 * cigarros_dia
total_carteiras = total_cigarros / 20
gasto = total_carteiras * preco_carteira

print(f'o gasto total é {gasto}')