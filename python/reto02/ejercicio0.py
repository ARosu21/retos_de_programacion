# Vamos a crear ejemplos de funciones básicas

# Función sin parámetros ni retorno
def sayHello():
	print("Hello!")

sayHello()

# Función con un parámetro
def sayHelloName(name):
	print(f"Hello {name}!")

sayHelloName("Adrian")

# Función con múltiples parámetros y retorno
def multiply(value1, value2):
	return value1*value2

print(multiply(5,3))	

# Comprobar si se pueden crear funciones dentro de funciones
def sayByeAndAdd(value1, value2):
	def addition(value1, value2):
		return value1+value2
	print("Bye!")
	print(addition(value1, value2))

sayByeAndAdd(2,3)

# Funciones incorporadas en python
print(max([1,2,3]))

# Variable global va definida fuera de las funciones y puede llamarse dentro de las funciones
variable_global = "Global"

# Variable local está definida dentro de una función y solo se le puede llamar desde dentro
def variables():
	variable_local = "Local"
	print(variable_global)
	print(variable_local)

variables()
