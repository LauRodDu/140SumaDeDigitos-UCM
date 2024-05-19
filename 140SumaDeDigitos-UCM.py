'''Suma de dígitos
Tiempo máximo: 1,000-4,000 s  Memoria máxima: 4096 KiB
Se trata de implementar un programa que sume los dígitos de un número entero no negativo. Por ejemplo, la suma de los dígitos del 3433 es 13.

Para darle un poco más de emoción, el programa no se limitará a escribir el resultado de la suma, sino que también escribirá todos los sumandos utilizados: 3 + 4 + 3 + 3 = 13.

Entrada
La entrada consta de una serie de casos de prueba terminados con un número negativo. Cada caso de prueba es una simple línea con un número no negativo no mayor que 109 del que habrá que sumar todos sus dígitos.

Salida
Para cada caso de prueba se mostrará una línea en la que aparecerán cada uno de los dígitos separados por el signo +, tras lo cual aparecerá el símbolo = y la suma de todos los dígitos.

Ten en cuenta que antes y después de cada símbolo (+ y =) hay un espacio.

Entrada de ejemplo   Salida de ejemplo
3433				 3 + 4 + 3 + 3 = 13
64323				 6 + 4 + 3 + 2 + 3 = 18
8					 8 = 8
-1'''

while True:
    numero = input().strip()
    n = int(numero)
    if n < 0:
        break

    digitos = [int(d) for d in numero]
    suma = sum(digitos)
    print(f"{' + '.join(numero)} = {suma}")
