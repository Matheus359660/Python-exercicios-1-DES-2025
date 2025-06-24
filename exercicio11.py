# criado por Matheus
# crie um programa que receba o peso (kg) e altura (m) de uma pessoa e calcule o IMC.
# clasifique o resultado de acordo com a faixa:

# °Abaixo do peso (<18.5)
# °Peso normal (18.5 a 24.9)
# °Sobrepeso (25 a 29.9)
# °Obesidade (>=30)
unidade = ("medida do peso")
peso = float(input("digite o peso (kg): "))
altura = float(input("digite a altura (m): "))

imc = peso / (altura **2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso.")
elif imc < 25:
    print("peso normal.")
else:
    print("acima do peso.")