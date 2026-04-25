'''
Escreva um programa que aceite uma frase como entrada e informe o
numero de vogais presentes na frase.
'''
frase_de_entrada = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = 0

for caractere in frase_de_entrada:
    if caractere in vogais:
        contador += 1

print(f"Número de vogais: {contador}")