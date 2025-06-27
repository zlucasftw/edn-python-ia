"""
4- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

try:

    temperatura = float(input("Digite o valor da temperatura: "))
    unidade_de_origem = input("Digite a unidade de origem (Celsius, Fahrenheit e Kelvin): ").lower()
    unidade_de_conversao = input("Digite a unidade para qual deseja converter (Celsius, Fahrenheit e Kelvin): ").lower()

    temperatura_convertida = 0

    temperaturas = ["celsius", "fahrenheit", "kelvin"]

    if unidade_de_origem in temperaturas[0]:
        if temperaturas[0] == unidade_de_conversao:
            temperatura_convertida = temperatura   # Celsius

        if temperaturas[1] == unidade_de_conversao:
            temperatura_convertida = (temperatura * 1.8) + 32  # Fahrenheit

        if temperaturas[2] == unidade_de_conversao:
            temperatura_convertida = temperatura + 273.15  # Kelvin

    elif unidade_de_origem in temperaturas[1]:

        if temperaturas[1] == unidade_de_conversao:
            temperatura_convertida = temperatura   # Fahrenheit

        if temperaturas[0] == unidade_de_conversao:
            temperatura_convertida = (temperatura - 32) / 1.8  # Celsius

        if temperaturas[2] == unidade_de_conversao:
            temperatura_convertida = (temperatura - 32) * (5 / 9) + 273.15  # Kelvin


    elif unidade_de_origem in temperaturas[2]:

        if temperaturas[2] == unidade_de_conversao:
            temperatura_convertida = temperatura   # Kelvin

        if temperaturas[0] == unidade_de_conversao:
            temperatura_convertida = temperatura - 273.15   # Celsius

        if temperaturas[1] == unidade_de_conversao:
            temperatura_convertida = ((temperatura - 273.15) * 1.8) + 32   # Fahrenheit

    if unidade_de_origem not in temperaturas or unidade_de_conversao not in temperaturas:
        print(f"Unidade de conversão inválida!")
    else:
        print(f"Temperatura convertida: {temperatura_convertida:.2f} graus {unidade_de_conversao}")

except ValueError:
    print("Valor de entrada incorreto")
