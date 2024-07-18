# Todos los valores ingresados por teclado siempre serán string
informacion = input('Por favor ingresa un número: ')


try:

    # print(10/0)
    informacion_numeros = int(informacion)
    print(informacion_numeros + 10)
    print(informacion)
except TypeError: 
    # Solo cuando error sea de tipo TypeError lanzará el error
    print('Hubo un error')
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except Exception as e:
    print(type(e))
    print('Ocurrió otro error')