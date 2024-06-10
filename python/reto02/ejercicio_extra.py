def imprimir(cadena1, cadena2):
	num_1 = 0
	num_2 = 0
	
	for i in range(1, 101):
		if i%3 == 0 and i%5 == 0:
			print(cadena1+cadena2)
			num_1 += 1
			num_2 += 1
		elif i%3 == 0:
			print(cadena1)
			num_1 += 1
		elif i%5 == 0:
			print(cadena2)
			num_2 += 1
		else:
			print(i)
	
	return num_1, num_2

num1, num2 = imprimir("Hola", "Adios")

print(f"Se ha impreso Hola: {num1} veces")
print(f"Se ha impreso Adios: {num2} veces")
