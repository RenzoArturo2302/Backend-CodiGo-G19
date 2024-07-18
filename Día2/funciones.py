# numero = 10

# # declaramos una función (definimos su comportamiento)
# def incrementar_en_uno():
#     print(1)

# # Llamamos a la ejecución de la función. Se tiene que poner los parámetros (que van entre paréntesis) y si no llama a la función esta no se ejecutará
# incrementar_en_uno()

# # Si bien nosotros podemos declarar los tipos de datos que recibe una función en los parámetros, estos no son de una manera determinante, es decir al final podemos pasar 
# # cualquier tipo de dato diferente al declarado.
# def calcular_promedio(numero1, numero2):
#     resultado = (numero1 + numero2) / 2
#     # La función devolverá un valor
#     return resultado
# resultado_promedio = calcular_promedio(10, 40)




# Crear una función en la cual se el nombre y que se retorne el saludo 'Buenas noches NOMBRE'
def saludar(nombre):
   return "Buenas noches " + nombre


nombre = "Juan"
saludo = saludar(nombre)
print(saludo)

def numeros(*args):
   print(args)


numeros(1,2,3,4,5,5,6,7,20)

# kwargs > key arguments | argumentos con llaves
def informacion(**kwargs): 
   print(kwargs)


informacion(nombre='Eduardo', casado = True, promedio = 19.3, direccion="Calle los florentinos 1050")

def combinada(*args, **kwargs): 
   print(args, kwargs)

combinada(10,40, True, 0, 'etc', curso='Backend', nota='Es mejor que frontend')