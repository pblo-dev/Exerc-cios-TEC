'''
Crie um programa para o usurário informar o peso e a altura de uma
determinada pessoa. Apossas a digitação calcular o IMC ( ı́ D ndice de massa
corporal ) da pessoa a Informar em que faixa ela se enquadra
'''
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * 2)
print(f'Seu IMC é: {imc:.2f}')

if imc < 20:
    print(f'Você está abaixo do peso ideal.')
elif imc > 25:
    print(f'Você está com sobre peso. Faça um regime.')
else:
    print(f'Você está no peso ideal.')