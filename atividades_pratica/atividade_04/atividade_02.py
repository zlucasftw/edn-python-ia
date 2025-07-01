"""
Crie um programa que permita a um professor registrar as notas de uma turma. O
programa deve continuar solicitando notas até que o professor digite 'fim'.
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""

media, soma, quantidade = 0, 0, 0

while True:
    try:

        notas = input("Digite as notas da turma ou fim para finalizar: ")

        if notas.lower() == "fim":
            if quantidade > 0:
                media = soma / quantidade
                print(f"A média da turma é de: {media:.2f}")
            else:
                print(f"A média da turma é de: {soma}")
            break

        notas = float(notas)
        if 0 <= notas <= 10:
            soma += notas
            quantidade += 1

    except ValueError:
        print("Digite um valor de entrada válido!")

