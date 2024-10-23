"""4. Escribe expresiones lógicas que cumplan las siguientes especificaciones y sea falsa en
el caso contrario al formulado:
1. Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a
60 euros pero igual o inferior a 420 euros.

precio = 300
print (precio >= 60 and precio <= 420)


2. Debe ser Verdadera si el número contenido en la variable entera número es impar.

numero = 21
print (numero % 2 != 0)

3. Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar
son válidas.

saldo = 40
dineroSacar = 50

if dineroSacar >=0 and dineroSacar <= saldo:
    print (True)
else: 
    print(False)"""



"""4. Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir,
que estén comprendidas entre 0:0 y 23:59.



hora = int(input("digitar hora: "))
minutos = int(input("digitar minutos: "))

if 0 <= hora <= 59 and 0 <= minutos <= 23:

    print ("la hora: ",  hora,":",minutos, "minutos es CORRECTA")

else : 
    
    print ("INCORRECTA")"""


"""5. Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una
persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).

estadoCivil = input("escriba la inicial de su estado civil : s si es Soltero, c si es Casado, v si es Viudo, d si es Divorciado")

if estadoCivil == "s" or estadoCivil == "C" or estadoCivil == "v" or estadoCivil == "d":
    print (False)
else :
    print (True) """


"""6. Debe ser Verdadera si el contenido de las variables enteras sueldo_bruto y
sueldo_neto es el adecuado para una retención del 22%.

sueldo_bruto = 100
sueldo_neto = 78

print (sueldo_bruto * .78 == sueldo_neto)"""





"""7. Debe ser Verdadera si el contenido de la variable entera día es un valor válido para
el mes de mayo.

dia = 32

print (1 <= dia <=31)


8. Debe ser Verdadera si el número contenido en las variables enteras num1 y num2
son múltiplos de tres.
num1 = -3
num2 = 27

print (num1 % 3 == 0 and num2 % 3 == 0)


9. Debe ser Verdadera si la calificación contenida en la variable real nota es un
aprobado. 

nota = 11

print (5 <= nota <=10)


10. Debe ser Verdadera si la media de la calificación contenida en las variables reales
nota1, nota2 y nota3 es un aproblado.

nota1 = 5
nota2 = 3
nota3 = 6

media = (nota1 + nota2 + nota3)/3
print ("la nota es: ", media, 5 <= media <=10)


Programación 2024/25
IES Jacarandá
5. Escribir una expresión lógica que cumpla el siguiente enunciado y sea verdadera en caso
contrario al formulado:

1. Debe ser Falsa cuando la variable cantidad que contiene la cantidad a retirar de un
cajero sea superior a 600 euros o presente un valor negativo.

cantidad_retirada = int(input("Ingrese la cantidad a retirar: "))

if (0>= cantidad_retirada or cantidad_retirada > 600):
    print ("falso, la cantida introducida no es permitida")
else :
    print ("verdadero, retito aceptado")



2. Debe ser Falsa si la edad de la persona se encuentra entre la población activa, es
decir, la variable está entre 18-65 años.


edad = int(input("ingrese su edad: "))

if 18<=edad <=65:
    print ("haces parte de la poblaciòn ACTIVA")
elif edad <= 0:
    print ("ingrese una edad valida")
    int(input("ingrese su edad: "))

else :
    print ("haces parti de la poblaciòn INACTIVA")

edad = int(input("ingrese su edad: "))

while edad <= 0 or edad >= 130:
    print ("ingrese una edad valida")
    edad = int(input("ingrese su edad: "))

if 18<=edad <=65:
    print ("haces parte de la poblaciòn ACTIVA")

else :
    print ("haces parti de la poblaciòn INACTIVA")





3. Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.

respuesta = input("Responde con S para Sí o N para No: ")

print ( not (respuesta == "s" or respuesta == "n"))"""


"""4. Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7
o de 3.

numero = int(input("digite un numero: "))

print (not(numero % 7 == 0 or numero % 3 == 0))

5. Debe ser Falsa si alguna de las calificaciones conteni das en las variables reales
nota1, nota2 y nota3 es un suspenso.

nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))

print (nota1 >= 5 and nota2 >= 5 and nota3 >= 5)


6. Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga
menos de 1000 euros en la variable saldo o se haya quedado al descubierto más de
5 veces. Este último dato se almacenará en la variable descubierto


saldo = 1200  
descubierto = 3  

if saldo < 1000 or descubierto > 5:
    usuario_fiable = False
else:
    usuario_fiable = True

if usuario_fiable:
    print("El usuario es fiable.")
else:
    print("El usuario no es fiable.")



7. Debe ser Falsa cuando el valor almacenado en la variable asignaturasAprobadas
sea inferior al 30% del valor almacenado en la variable asignaturasCurso.

8. Debe ser Falsa si los números contenidos en las variables enteras mes y día no son
válidos. Vamos a considerar que no hay años bisiestos.^

mes = int(input("ingrese el mes en numero: "))
dia = int( input()"ingrese el dia: ")

enero = 1
febrero = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8
septiembre = 9
octubre = 10
noviembre = 11
diciembre = 12 


if (mes == 1 and dia <= 31) or (mes == 2 and dia <= 28) or (mes == 3 and dia <= 31) or (mes == 4 and dia <=30 ) or (mes == 5 and dia <= 31) or (mes == 6 and dia <= 30):
    print ("la fecha es valida")
else:
    print ("la fecha es invalida")





6. Determina para qué valores de las variables llueve, haceSol y haceFrio es cierta la
siguiente expresión sin calcular su tabla de verdad. Comprueba el resultado en python:
llueve y no haceSol y no haceFrio o no llueve y haceSol y no haceFrio o no llueve y
no haceSol y haceFrio


llueve = True
hacesol = False
hacefrio = False

print (llueve and not hacesol and not hacefrio or not llueve and hacesol and not hacefrio or not llueve and
not hacesol and hacefrio)


7. A partir de los dos enunciados siguientes, expresa en castellano el significado de las
siguientes expresiones lógicas:
a: Me gusta programar
b: Voy a dedicar al menos diez horas a la semana a programar
1. not a and b     R/ No me gusta programar y voy a dedicar al menos diez horas a la semana a programar.
2. not a or b      R/ No me gusta programar o voy a dedicar al menos diez horas a la semana a programar
3. not not a       R/ Me gusta programar
4. not a or not b  R/No me gusta programar o no voy a dedicar al menos diez horas a la semana a programar
5. not (a or b)    R/No me gusta programar y no voy a dedicar al menos diez horas a la semana a programar
6. not a and not b R/No me gusta programar y no voy a dedicar al menos diez horas a la semana a programar"""
