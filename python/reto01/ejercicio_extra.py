# Imprimir números entrer 10 y 55, pares y que no sea ni el 16 ni múltiplos de 3

for number in range(10,56):
    if number != 16 and number%3 != 0 and number%2 == 0:
        print(number)
