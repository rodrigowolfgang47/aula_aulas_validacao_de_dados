from random import  randint

quadrado = 0
triangulo = 0
circulo = 0
hexagono = 0

for i in range (1000000):
    numero_aleatorio = randint(1, 4)
    if (numero_aleatorio == 1):
        quadrado += 1
    elif (numero_aleatorio == 2):
        triangulo += 1
    elif (numero_aleatorio == 3):
        circulo += 1
    else:
        hexagono += 1

print(f'Quadrado teve {(quadrado/1000000)*100}% \n'
      f'Triangulo teve {(triangulo/1000000)*100}% \n'
      f'Circulo teve {(circulo/1000000)*100}% \n'
      f'hexagono teve {(hexagono/1000000)*100}% \n')