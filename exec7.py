# programa para lera as dimensões de uma piscina em formato retangular
# (largura, comprimento e profundidade), com isso o programa deve exibir o volume de
# água da piscina, a seguir calcule o tempo para encher a piscina levando em conta que
# você possui uma bomba de água que possui uma vazão de 20 metros cúbicos por
# minuto, imprima o resultado na tela.

largura = float(input('Digite a largura da piscina: '))
comprimento = float(input('Digite a comprimento da piscina: '))
profundidade = float(input('Digite a profundidade da piscina: '))

volume = largura * comprimento * profundidade

print(volume)

tempo_de_enchimento = (volume / 20)
print(f'A piscina comporta {volume:.2f} metros cúbicos de água, e demorará {tempo_de_enchimento:.2f} horas para encher.')