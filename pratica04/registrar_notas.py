"""
Crie um programa que permita a um professor registrar as notas de uma turma.
O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas
válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""

notas = []
while True:
    try:
        entrada = input("Digite a nota do aluno ou fim para encerrar: ")
        if entrada == 'fim':
            break
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Por favor, digite uma nota válida entre 0 e 10: ")
    except ValueError:
        print("Nota inválida. Digite um valor entre 0 e 10.")
if notas:
    media = sum(notas) / len(notas)
    print(f"""A média da turma: {media:.2f}
O total de notas registradas é: {len(notas)}
""")
else:
    print("Nenhuma nota foi registrada.")
