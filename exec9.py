# Escreva um programa que receba três números inteiros e informe qual deles é o maior.
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")
c = input("Digite o terceiro  número: ")

if a > b and a > c:
    print("O maior número é: ", a)
elif b > a and b > c:
    print("O maior número é ", b)
else:
    print("O maior número é ", c)
