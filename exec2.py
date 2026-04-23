#Receba uma temperatura em Fahrenheit e a converta para Celsius
temperatura_f = float(input("Digite a temperatura em Fahrenheit: "))
temperatura_c = (temperatura_f - 32) / 1.8
print(f'A temperatura em Celsius é: {temperatura_c:.2f}ºC')