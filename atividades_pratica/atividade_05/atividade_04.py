"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de
nascimento.
"""
import datetime


def calcula_idade(ano_nascimento : int):

    ano_atual = datetime.date.today().year
    dias_totais = 0

    while ano_nascimento < ano_atual:

        # if ano_nascimento == ano_atual:
        #     inicio_ano = datetime.datetime(datetime.date.today().year, 1, 1)
        #     agora_ano = datetime.datetime(datetime.date.today().day, datetime.date.today().month,
        #     datetime.date.today().year)
        #     dias_ano = agora_ano - inicio_ano
        #     print(dias_ano)

        if ano_nascimento % 4 == 0 or (ano_nascimento % 100 == 0 and ano_nascimento % 400 == 0):
             dias_totais += 366
        else:
            dias_totais += 365
        ano_nascimento += 1

    return dias_totais


try:

    ano = int(input("Digite o seu ano de nascimento: "))
    print(f"Sua idade em dias é de {calcula_idade(ano)} para o ano {ano}")

except ValueError:
    print("Digite o seu ano de nascimento!")
