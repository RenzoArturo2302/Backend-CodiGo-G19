# Colección de datos es una variable que puede guardar varios valores
# Listas (List) (arreglo)

frutas = ['manzana','plátano','papaya', 'granadilla','papaya']
#  Ordenada (tienen un indice de búsqueda)

print(frutas[0])

# Agrega elemento al final
frutas.append('uva')

print(frutas)

# Elimina elemento de la lista según su índice y retorna su valor
fruta_eliminada  = frutas.pop(0)
# Elimina elemento según el valor. Solo elimina el primer valor encontrado.
frutas.remove('papaya')
#  Si no existe ningún elemento con ese valor, lanzará un error
# frutas[6] = 'fresa' - No se puede utilizar un indice que no existe para reemplazar un elemento
print(fruta_eliminada)
print(frutas)


texto = 'Hola soy su profe'
print(len(texto))

print(len(frutas))


# Tuplas
# Es ordenada 
# No se puede editar (uneditable)
meses = ('Enero', 'Febrero', 'Marzo')

# Mantener el mismo contenido durante toda la ejecución del archivo o programa


# Sets
# Es desordenada
# Si es editable

alumnos = {'Abel', 'Christian', 'Denys', 'Andree', 'Giancarlo', 'Ignacio' }

print(alumnos)

# Para agregar elementos
 
alumnos.add('Arnold')

print(alumnos)

# Diccionarios

persona = {
    'nombre': 'Renzo',
    'hobbies': ['Comer', 'Dormir'],
    'direccion': {
        'calle': 'calle las paltas',
        'numero': 2023
    },
    'casado': False
}

# Si utilizamos una key que no existe, creará esa nueva key. En caso contrarío reemplazará el valor antiguo
print(persona['nombre'])
print(len(persona['hobbies']))
print(persona['direccion']['calle'])
