import csv
with open("dados.csv", "w") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['nome','idade','cidade'])
    escritor.writerow(['Maria','30','Salvador'])

