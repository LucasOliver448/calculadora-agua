litros_por_dia = float(input("Ditite a quantidade de litros consumidos por dia: "))
numero_de_pessoas = int(input("Digite o numero de pessoas na residencia: "))
preco_m3 = float(input("Digite o preço do metro cúbico de água: "))
consumo_m3 = (litros_por_dia * 30 * numero_de_pessoas) / 1000
custo_mensal = consumo_m3 * preco_m3
print(f"O consumo mensal de água é de {consumo_m3:.2f} m3 e o custo mensal é de R$ {custo_mensal:.2f}.")

