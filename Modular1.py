
"""1. Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).
"""

list=[]
from random import randint
numero = randint (0,5)
x=0
for i in range (1,10):
  from random import randint
  numero = randint (0,5)
  x += list.append(numero)

  if x>x:
    print(x)

"""2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.)."""


lista = []
for i in range (0,10):

    var1=int(input("diga un numero: "))
    if i==9:
        lista.insert(0,var1)
    else:
        lista.insert(i,var1)
print(lista)

"""3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo."""

dia= int(input("instroducir el dia:"))
mes=int(input("introducir el mes: "))
año=int(input("introducir el año: "))

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "Agosto", "septiembre", "Octubre", "Noviembre", "Diciembre",]

while (dia>=30 or dia<=0) or (mes>=12 or mes<=0) or año<=0:
  print("uno o mas datos son incorrectos")
  dia= int(input("vuelva a instroducir el dia:"))
  mes=int(input("vuelva a introducir el mes: "))
  año=int(input("vuelva a introducir el año: "))

while dia > 0:
   print(f"la fecha es:{dia} de {meses[mes-1]} de {año}")
   dia= int(input("vuelva a instroducir el dia y si quiere salir introduzca el dia en negativo o 0:"))
   mes=int(input("vuelva a introducir el mes: "))
   año=int(input("vuelva a introducir el año: "))
  
print("termino")

"""4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares."""
listaNumeros=[]
numero=int(input("Dime un número: "))
if numero % 2==0:
    print(f"El número {numero} es par ")
else:
    print(f"El número {numero} es impar")
listaNumeros.append(numero)
mayor=listaNumeros[0]
while numero >= 0:
    numero=int(input("Dime un número: "))
    if numero % 2==0:
        print(f"El número {numero} es par ")
    else:
        print(f"El número {numero} es impar")
    listaNumeros.append(numero)
print(listaNumeros)
for i in range(len(listaNumeros)):
    if listaNumeros[i] > mayor:
        mayor=listaNumeros[i]
print(f"El número mayor es {mayor}") 

"""5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]."""





 

  
 