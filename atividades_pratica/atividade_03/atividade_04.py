"""
4- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

try:

    temperatura = float(input("Digite o valor da temperatura: "))
    unidade_de_origem = input("Digite a unidade de origem (Celsius, Fahrenheit e Kelvin): ")
    unidade_de_conversao = input("Digite a unidade para qual deseja converter (Celsius, Fahrenheit e Kelvin): ")

    temperatura_convertida = 0

    temperaturas = ["Celsius", "Fahrenheit", "Kelvin"]

    if unidade_de_origem in temperaturas:
        if unidade_de_conversao in temperaturas:
            temperatura_convertida = (temperatura * 1.8) + 32   # Fahrenheit

        if unidade_de_conversao in temperaturas:
            temperatura_convertida = temperatura + 273.15   # Kelvin
    elif unidade_de_origem == temperaturas:
        if unidade_de_conversao == temperaturas:
            temperatura_convertida = (temperatura - 32) / 1.8   # Celsius

        if unidade_de_conversao in temperaturas:
            temperatura_convertida = (temperatura - 32) * 5 / 9 + 273   # Kelvin
    elif unidade_de_origem in temperaturas:
        if unidade_de_conversao == temperaturas:
            temperatura_convertida = temperatura - 273.15   # Celsius

        if unidade_de_conversao == temperaturas:
            temperatura_convertida = (temperatura - 273) * 1.8 + 32     # Fahrenheit

    if unidade_de_origem not in temperaturas:
        print(f"Unidade de conversão inválida!")
    else:
        print(f"Temperatura convertida: {temperatura_convertida} Graus {unidade_de_conversao}")

except ValueError:
    print("Valor de entrada incorreto")
