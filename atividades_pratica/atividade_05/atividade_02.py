"""
Crie uma função que verifique se uma palavra ou frase é um
palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação).

Se o resultado é True, responda “Sim”, se o resultado for
False, responda “Não
"""
import string


def verifica_palindromo(palavra : str):
    palavra = "".join([letr for letr in palavra.lower().replace(" ", "") if letr not in string.punctuation])
    palavra_inversa = "".join([letra for letra in reversed(palavra.lower().replace(" ", "")) if letra not in string.punctuation])

    if palavra in palavra_inversa:
        return True
    else:
        return False



try:
    texto_digitado = str(input("Digite uma palavra ou frase e veja se é um palíndromo: "))

    if verifica_palindromo(texto_digitado):
        print("Sim")
    else:
        print("Não")
except ValueError:
    print("Erro na entrada de dados!")

