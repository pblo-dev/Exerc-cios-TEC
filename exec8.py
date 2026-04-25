'''
Faça um programa para ler o valor de uma conta em um
restaurante/Lanchonete, depois disso o programa deve perguntar quanto em
porcentagem você quer dar de gorjeta, o programa ao final deve informar o total a ser
pago e quanto desse total é o valor da gorjeta.
'''
valor_consumo = float(input('Digite o valor da conta: '))
porcentagem_gorjeta = float(input('Qual porcentagem da gorjeta? Recomenado: 10% - '))
valor_gorjeta = (porcentagem_gorjeta/100) * valor_consumo
valor_total = valor_consumo + valor_gorjeta
print(f'O valor da conta é {valor_total:.2f} reais, sendo {valor_gorjeta:.2f} reais o valor da gorjeta.')