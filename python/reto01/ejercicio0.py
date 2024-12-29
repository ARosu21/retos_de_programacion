# Vamos a crear ejemplos de todos los operadores lógicos de python

# Operador and
print(True and True)
print(True and False)

# Operador or
print(True or True)
print(False or True)

# Operador not
print(not True)
print(not False)
print(not not True)

# Operadores artiméticos
print(12+3) #Suma ambos valores
print(12-3) #Resta ambos valores
print(12*3) #Multiplica ambos valores
print(12/3) #Divide ambos valores
print(16%3) #Módulo de la división, devuelve el resto
print(12**3) #Eleva a la potencia indicada
print(18//5) #Divide y devuelve el resultado entero, sin decimales

# Operadores relacionales
print(12>3) #Valor de la izquierda mayor que la derecha, True
print(12<3) #Valor de la izquierda menos que la derecha, True
print(12==3) #Si ambos valores son iguales, True
print(12>=3) #Valor de la izquierda mayor o igual que la derecha, True
print(12<=3) #Valor de la izquierda menor o igual que la derecha, True
print(12!=3) #Valor de la izquierda diferente a la derecha, True

# Operadores bit a bit
a = 10 #1010
b = 3 #0011
print(a & b) #Hace el AND bit a bit de ambos números
print(a | b) #Hace el OR bit a bit de ambos números
print(a ^ b) #Hace eñ XOR bit a bit, si los dos son iguales 1 si son diferentes 0
print(~a) #Hace el NOT bit a bit
print(a >> 2) #Desplaza a la derecha los bits el número de veces indicado, en este caso 2 a la derecha y rellena con ceros
print(a << 2) #Desplaza a la izquierda los bits el número de veces indicado, en este caso 2 a la derecha y rellena con ceros

# Ahora vamos a crear ejemplos de los tipos de estructuras de control

# Condicional if-elif-else
if True == True and False == False:
    print("Se ha cumplido el if con AND")
elif True == False or True == True:
    print("Se ha cumplido el if con OR")
elif True == (not False):
    print("Se ha cumplido el if con NOT")
else:
    print("No se ha cumplido ninguno")

# Ciclo for
numeros = [1, 2, 3]
for i in numeros:
    if i > 0:
        print(i)

# Ciclo while
x = 1
while x < 5:
    print(x)
    x += 1

# Sentencia try-except
try:
    if True == True:
        c = "cadena"
except SyntaxError:
    print("Error de sintaxis")
