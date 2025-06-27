"""
3- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"

< 25: classificacao = "Peso normal"

< 30: classificacao = "Sobrepeso"

Para os demais cenários: classificacao = "Obeso"
"""

try:
    peso_em_kg = float(input("Digite seu peso em kilogramas (KG): "))
    altura_em_metros = float(input("Digite sua altura em metros (m): "))

    imc = peso_em_kg / (altura_em_metros * altura_em_metros)

    classificacao = "Classificação:"
    if imc < 18.5:
        print(f"{classificacao} Abaixo do peso")
    elif imc < 25:
        print(f"{classificacao} Peso normal")
    elif imc < 30:
        print(f"{classificacao} Sobrepeso")
    else:
        print(f"{classificacao} Obeso")

except ValueError:
    print("Digite apenas valores númericos!")