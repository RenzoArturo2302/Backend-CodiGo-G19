# for
# repetitivo debe tener un final


# posición inicial hasta menor que el límite (10)
for numero in range(0, 10):
    print(numero)

print("=======")
for numero in range(5):
    print(numero)


print("=======")

for numero in range(1, 10, 2):
    print(numero)

print("=======")

notas = [10,15,6,14,18,20]

for nota in notas: 
    print(nota)
print("=======")
texto = "El día de hoy fue un día muy frio ya que estamos en invierno"

for letra in texto:
    print(letra)



notas = [15, 7, 12, 14, 20]

notas_aprobadas = []
notas_desaprobadas = []

for nota in notas:
    if nota <= 10:
        notas_desaprobadas.append(nota)
    elif nota <= 20: 
        notas_aprobadas.append(nota)

def promedio (lista_notas):
    suma_notas = 0
    for nota in lista_notas:
        suma_notas += nota
    return suma_notas / len(lista_notas)



print(notas_aprobadas)
print(promedio(notas_aprobadas))
print("Aprobados: ", len(notas_aprobadas))


print(notas_desaprobadas)
print(promedio(notas_desaprobadas))
print("Desaprobados: ", len(notas_desaprobadas))





# while
tope = 100
inicio = 0

while inicio < tope:
    print(inicio)
    inicio+=1


    