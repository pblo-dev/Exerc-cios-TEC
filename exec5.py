#programa que calcule área de um quadrado, área de um trapézio e a área de um triângulo e informe qual tem maior área
lado = input("Digite o valor do lado do quadrado: ")
base_maior = input("Digite o valor da base maior do trapézio: ")
base_menor = input("Digite o valor da base menor do trapézio: ")
altura_trapezio = input("Digite o valor da altura do trapézio: ")
base_triangulo = input("Digite o valor da base do triângulo: ")
altura_triangulo = input("Digite o valor da altura do triângulo: ")
area_quadrado = float(lado) ** 2
area_trapezio = ((float(base_maior) + float(base_menor)) * float(altura_trapezio)) / 2
area_triangulo = (float(base_triangulo) * float(altura_triangulo)) / 2
if area_quadrado > area_trapezio and area_quadrado > area_triangulo:
    print("O quadrado tem a maior área: ", area_quadrado)
elif area_trapezio > area_quadrado and area_trapezio > area_triangulo:
    print("O trapézio tem a maior área: ", area_trapezio)
else:    print("O triângulo tem a maior área: ", area_triangulo)