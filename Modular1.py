
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
aleatorios = []

for i in range(1000):
    from random import randint
    aleatorios.append(randint(0,1000))

print(aleatorios)

# Funciones

def obtener_mayor(lista_numeros):
    elementoMayor = lista_numeros[0]

    for i in range(len(lista_numeros)):
        if lista_numeros[i] > elementoMayor:
            elementoMayor = lista_numeros[i]


    return elementoMayor

def obtener_menor(lista_numeros):
    elementoMenor = lista_numeros[0]

    for i in range(len(lista_numeros)):
        if lista_numeros[i] < elementoMenor:
            elementoMenor = lista_numeros[i]

    return elementoMenor



def suma(listaValoresASumar):
    sumaTotal = 0
    for i in range(len(listaValoresASumar)):
        sumaTotal+=listaValoresASumar[i]


    return sumaTotal


def calcularMedia(elementos):
    return suma(elementos)/len(elementos)



def sustituirValor(lista, numeroABuscar, numeroSustituto):
    for i in range(len(lista)):
        if lista[i]==numeroABuscar:
            lista[i]=numeroSustituto

    return lista



print("Introduzca una opción: ")
print('''           a. Conocer el mayor
            b. Conocer el menor
            c. Obtener la suma de todos los números
            d. Obtener la media
            e. Sustituir el valor de un elemento por otro número introducido por teclado
            f. Mostrar todos los números
            g. Salir
            ''')
opcion = input("")

while opcion!="g":
    if opcion=="a":
        print(obtener_mayor(aleatorios))
    elif opcion=="b":
        print(obtener_menor(aleatorios))
    elif opcion=="c":
        print(suma(aleatorios))
    elif opcion=="d":
        print(calcularMedia(aleatorios))
    elif opcion=="e":
        nBuscar = int(input("¿Qué número quiere sustituir?"))
        nSustituir = int(input("¿Qué número le sustituye?"))
        sustituirValor(aleatorios, nBuscar, nSustituir)
    elif opcion=="f":
        print(aleatorios)
    
    opcion=input("Introduzca una opción (a-f, g para salir): ")




usuarios= []

for i in range(1000):
    usuarios.append("a")

"""2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.)."""
def listaOrdenada(lista):
    lista = []
    for i in range (0,10):
        var1=int(input("diga un numero: "))
        if i==9:
         lista.insert(0,var1)
        else:
         lista.insert(i,var1)
    return(lista)
print(listaOrdenada(lista))


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


usuario = input("ingresa una lista separada por guiones: ")
lista = usuario.split("-")

v_tipoStrig = ""
v_tipoStrig2 = str()
v_tipolist = list()


numero1 = "25"
numero2 = "2"
print(int(numero1)+int(numero2))


v_tipolist.i

def listaRever(lista):
    rever=[]
    for i in range (len(lista)):
     var=lista[len(lista)-i-1]
     rever.append(var)
    return rever

print(listaRever(lista))



"""6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario."""

lista = [9,2,5,8,9]

def estaOrdenada(lista):
    if len(lista) <= 1:
        return True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
print(estaOrdenada(lista))


"""7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato"""

ficha1 = [1, 4]
ficha = [2, 0]

def encajan(ficha,ficha1):
    return ficha[0] == ficha1[0] or ficha[0] == ficha1[1] or ficha [1] == ficha1 [0] or ficha [1] == ficha1 [1]
   
print(encajan(ficha1,ficha))



"""8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números."""


def factorial(numero):
    resultado = 1
    
    for i in range(1, numero+1):
        resultado*=i #resultado=resultado*i

    return resultado


def factorial_recursivo(numero):
    return 1 if numero==0 else numero*factorial_recursivo(numero-1)



lista = [15, 5, 4, 6, 7]
listaFactoriales = []

for numero in lista:
    listaFactoriales.append(factorial(numero))



def esPrimo(numero):
    primo = True

    for i in range(2, numero):
        if numero%i==0:
            primo = False

    return primo

def esPrimoWhile(numero):
    primo = True

    contador=2

    while contador<numero and primo:
        if numero%contador==0:
            primo = False
        contador+=1

    return primo


print(esPrimoWhile(1000000000000000000000000000000000000000000000000000000000))

assert(not esPrimo(4))
assert(not esPrimo(9))

assert(esPrimo(17))
assert(esPrimo(19))
print("Primos ok")


print(lista)
print(listaFactoriales)

assert(factorial(5)==120)
assert(factorial(6)==720)
assert(factorial(0)==1)
assert(factorial(1)==1)
assert(not factorial(5)!=120)

print("Han pasado todos los tests!!")

print(factorial(50))

  
"""9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k."""

lista = [1,5,20,13,100, 55, 28]
k = 10


def listaMenorMayorMultiplo (lista):
    listaMenores = []
    listaMayores = []
    listaMultiplos = []

    for i in range (len(lista)):
        if lista[i] < k:
            listaMenores.insert (i, lista[i])
        elif lista [i] > k:
            listaMayores.insert(i,lista[i])
        if lista[i] % k == 0 :
            listaMultiplos.insert (i, lista[i])

    return(listaMenores, listaMayores, listaMultiplos)
print(listaMenorMayorMultiplo(lista))


"""10. Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1."""


def conversor(numero):
    if numero[-1] == 'D':
        decimal = int(numero[:-1])
        binario = bin(decimal)[2:]  
        return f"{binario}B"
    elif numero[-1] == 'B':
        binario = numero[:-1]
        if all(digit == '0' or digit == '1' for digit in binario):
            decimal = int(binario, 2)  
            return f"{decimal}D"
        else:
            return "Número binario no válido"
    else:
        return "Formato no válido"

numero1 = "1010B"
numero2 = "23D"
numero3 = "1020101B"

print(conversor(numero1))
print(conversor(numero2))
print(conversor(numero3))


"""11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno"""

lista1 = [7, 10, 2, 4, 8, 33]
lista2 = [2, 33, 2, 10]

#if len(lista1) > len(lista2):
def listaIguales (lista1, lista2):
 listaIguales = []
 for n in range (len(lista2)):
   for i in range (len(lista1)):
      if lista2[n]==lista1[i]:
        listaIguales.append(lista2)
   return (listaIguales)
        
print(listaIguales(lista1, lista2))


"""13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos."""


listaNombre = ["pedro", "antonio", "pablo", "martin", "poncho", "frank", "franklin"]
letra = "f"

def listaNueva (listaNombre, letra):
 listaN = " "
 listaNueva = []
 for i in range (len(listaNombre)):
   listaN = listaNombre [i]
   if listaN[0] == letra:
    listaNueva.append(listaN)
 return listaNueva
    
print (listaNueva(listaNombre, letra))