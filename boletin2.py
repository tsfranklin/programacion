"""Boletín 2. Estructuras condicionales.
1. Realizar un programa que lea un número entero por teclado e informe de si el número es
par o impar (el cero se considera par).


num = int(input("ingresa un numero entero: "))


if num % 2 == 0 :
   print ("el numero es par")
else:
   print ("el numero es impar")


2. Realizar un programa que solicite dos números e informe si son iguales, el primero mayor
que el segundo o el primero más pequeño que el segundo.


num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa el segundo numero: "))


if num1 == num2 :
   print ("los numeros %s y %s son iguales" %(num1,num2))
elif num1 > num2 :
   print ("el numero %s es mayor que el numero %s " %(num1, num2))
else:
   print("el numero %s es menor que el segundo %s " %(num1, num2))




3. Realizar un programa que lea un número por teclado. El programa debe imprimir en
pantalla un mensaje con “El número xx es múltiplo de 2” o un mensaje con “El número xx es
múltiplo de 3”. Si es múltiplo de 2 y de 3 deben aparecer los dos mensajes. Si no es múltiplo
de ninguno de los dos el programa finaliza sin mostrar ningún mensaje.



num = int(input("ingresa un numero: "))


if (num % 2 == 0) and (num % 3 == 0):
   print("el numero ", num, " es multiplo dos y de tres")
elif num % 2 == 0 :
   print ("el numero ", num, " es multiplo dos")
elif num % 3 == 0:
   print ("el numero ", num, " es multiplo tres")
#else :
 #  print ("no es multiplo de 3 y no es multiplo de 2")


4. Realiza un programa que reciba la edad de una persona (entre 0 y 50 años) y comunique
la etapa educativa que le corresponde:
- 0 a 6 años: Educación infantil.
- 7 a 11 años: Educación primaria.
- 12 a 16 años: Educación secundaria obligatoria.
- Superior a 16 años: Enseñanza post-obligatoria.


edad = int(input("dime tu edad: "))


if 0 <= edad <=50 :
   if edad <=6 :
       print("Educación infantil")
   elif 7<= edad <= 11 :
       print ("Educación primaria")
   elif 12<= edad <= 16 :
       print ("Educación secundaria obligatoria")
   else:
       print("Enseñanza post-obligatoria")


else:
   print("esta fuera del rango")




5. Realizar un programa que solicite 4 números e imprima la media de los números, cuántos
son superiores a la media y sus valores.
Por ejemplo, dados: 5, 4, 9, 6 ⇒ La media es 6 y hay 1 número/s superior a la media: 9.


num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
num3 = int(input("ingresa un numero: "))
num4 = int(input("ingresa un numero: "))


media = (num1 + num2 + num3 + num4)/4
cantidad = 0

superiores = " "
#for i in range (5) :
if num1 > media:
   cantidad+=1
   superiores+= str(num1) + ", "
if num2 > media:
   cantidad+=1
   superiores+= str(num2)+ ", "
if num3 > media:
   cantidad+=1
   superiores+= str(num3)+ ", "
if num4 > media:
   cantidad+=1
   superiores+= str(num4)
if superiores==" ":
   print("la media es: ", media, "y no hay numero superir a la media")
else:
   print ("la media es", media, " hay", cantidad, " numeros mayores que la media, son: ", superiores)




6. Diseña un programa que reciba dos números enteros y nos diga si son múltiplos entre sí,
es decir, si uno de ellos es múltiplo del otro.
Por ejemplo, dados: 36 y 9 respondería que sí son múltiplos, pero dados 15 y 24
respondería que no lo son.


num1 = int(input("dime un numero entero: "))
num2 = int(input("dime otro numero entero: "))

if num1 % num2 == 0:
    print("%s es multimplo de %s" %(num1, num2))
elif num2 % num1 == 0:
    print("%s es multimplo de %s" %(num2, num1))
else:
    print("No son múltiplos entre sí")


7. Realizar un programa que solicite un carácter por teclado e informe por pantalla si el
carácter es una vocal o no lo es. Si es una vocal mostrará el mensaje “Es la primera vocal
(A)” o “Es la segunda vocal (E)”. Puedes hacer que este programa no sea sensible a
mayúsculas.

caracter = input(" ingresa un caracter:  ")

if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "o" or caracter == "u":
    print("el caracter es una vocal")
else :
    print("el caracter no es una vocal")



8. Realizar un programa que lea el estado civil de una persona (S-Soltero, CCasado,
V-Viudo o D-Divorciado) y su edad. Después debe mostrar por pantalla el porcentaje de
retención que debe aplicarse de acuerdo con las siguientes reglas:
● A los solteros o divorciados menores de 35 años, un 12%
● Todas las personas mayores de 50 años, un 8.5%
● A los viudos o casados menores de 35 años, un 11.3%
● Al resto de casos se le aplica un 10.5%

edad = int(input("diga su edad: "))
estado_Civil = input("diga cual es su estado civil presiones S-Soltero, C-Casado, V-Viudo o D-Divorciado: ")

if 1 <= edad < 35 and ( estado_Civil == "s" or estado_Civil =="S" or estado_Civil =="d" or estado_Civil =="D"):
    print("aplica descuento del 12%")
elif 1 <= edad < 35 and (estado_Civil =="v" or estado_Civil =="V" or estado_Civil =="c" or estado_Civil =="C"):
    print("aplica descuento del 11.3%")
elif edad > 50 :
    print("aplica descuento del 8.5%")
elif 35 <= edad <=50:
    print("aplica descuento del 10.5%")
else :
    print("datos erroneos")



9. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error.
Programación 2024/25



dia_semana = (input("dime un numero del 1 al 7 y te dire el día correspondiente de la semana: "))

if dia_semana == "1":
    print("el dia es lunes")
elif dia_semana == "2":
    print("el dia es martes")
elif dia_semana == "3":
    print("el dia es miercoles")
elif dia_semana == "4":
    print("el dia es jueves")
elif dia_semana == "5":
    print("el dia es viernes")
elif dia_semana == "6":
    print("el dia es sabado")
elif dia_semana == "7":
    print("el dia es domingo")
else:
    print("ERROR el dato no corresponde a un dia de la semana ")


IES Jacarandá Brenes
10. Realizar un programa que lea por teclado dos marcaciones de un reloj digital (horas,
minutos, segundos) comprendidas entre las 0:0:0 y las 23:59:59 e informe cuál de ellas es
mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:36:36
“Hora 2 es mayor”


hora1 = int(input("digite la primera hora: "))
minutos1 = int(input("digite los minutos: "))
segundos1 = int(input("digite los segundos: "))

hora2 = int(input("digite la segunda hora: "))
minutos2 = int(input("digite los minutos: "))
segundos2 = int(input("digite los segundos: "))

if hora1 == hora2:

   if minutos1== minutos2:
         
      if segundos1 == segundos2:
       print("las horas son iguales")
      elif segundos1 > segundos2 :
        print ("hora 1 es mayor")
      else :
         print (" hora 2 es mayor")

   elif minutos1 > minutos2 :
    print ("hora 1 es mayor")
   else :
    print (" hora 2 es mayor")

elif hora1 > hora2 :
    print ("hora 1 es mayor")
else :
    print (" hora 2 es mayor")




11. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El porcentaje de
rebaja que se aplicará sobre el precio original del producto se calcula de la siguiente forma:
1. Si el producto es de tipo A, independientemente de su precio se aplica un 7% de
descuento.
2. Si el producto es de tipo C o bien el precio es inferior a 500€ se aplicará un
porcentaje del 12% de descuento.
3. En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y precio original) y
calcule el precio rebajado. Debe comprobarse que los datos de entrada son correctos, y si
no lo son mostrar un mensaje de error.

tipoDeProducto = input("indique el tipo de producto si es A, B o C: ")
precioOriginal = float(input("indique el precio original del producto: "))


if tipoDeProducto == "A" or tipoDeProducto == "a":
    descuento = precioOriginal * .93 
elif tipoDeProducto == "C" or tipoDeProducto == "c" or precioOriginal < 500:
    descuento = precioOriginal * .88
else:  tipoDeProducto == "B" or tipoDeProducto == "b" and precioOriginal >= 500 #no es necesario el precioOriginal >= 500
    
    
12. Realizar un programa que lea un carácter y dos números enteros por teclado. Si el
carácter leído es un operador aritmético, deberá calcular la operación correspondiente, si es
cualquier otro deberá mostrar la concatenación de los tres valores.

caracter = input("ingresar carácter:")
num1 = int(input("ingresa numero: "))
num2 = int(input("ingresa numero: "))

if caracter == "+":
    resultado = num1 + num2
    print(str(num1) + caracter + str(num2) + "= " + str(resultado))
elif caracter == "-":
    resultado = num1 - num2
    print(str(num1) + caracter + str(num2) + "= " + str(resultado))
elif caracter == "*":
    resultado = num1 * num2
    print(str(num1) + caracter + str(num2) + "= " + str(resultado))
elif caracter == "/":
    resultado = num1 / num2
    print(str(num1) + caracter + str(num2) + "= " + str(resultado))
else:
    print(str(num1) + caracter + str(num2))


13. Diseñar un algoritmo que nos diga el dinero total que tenemos después de pedirnos
cuantas monedas tenemos de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

moneda2euro = int(input("cuantas monedas tienes de 2€: "))
moneda1euro = int(input("cuantas monedas tienes de 1€: "))
moneda50centimo = int(input("cuantas monedas tienes de 50€: "))
moneda20centimo = int(input("cuantas monedas tienes de 20€: "))
moneda10centimo = int(input("cuantas monedas tienes de 10€: "))

dinero_total = moneda2euro * 2 + moneda1euro * 1 + moneda50centimo * .50 + moneda20centimo * .20 + moneda10centimo * .10 

print("en total tienes en euro: ", dinero_total )


14. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es
un número divisible por 4, pero no es divisible por 100, excepto que también sea divisible
por 400.


año = int(input("Diga el año: "))

if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

15. Realiza un algoritmo que calcule la potencia, para ello deberá pedir por teclado la base y
el exponente. Pueden ocurrir tres cosas:
- El exponente sea positivo, sólo tienes que imprimir la potencia.
- El exponente sea 0, el resultado es 1.
- El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = float(input("digite la base: "))
exponente = float(input("digite el exponente: "))

if exponente > 0:
    resultado = base**exponente
    print(f"{base}**{exponente}={resultado}")
elif exponente == 0 :
    print(f"{base}**{exponente}=1")
elif exponente < 0:
    resultado=1/(base**(-exponente))
    exponentePositivo = -(exponente)
    print(f"1/({base}**{exponente})={resultado} o 1/({base}**{exponentePositivo}) ")
    



16. Crea un programa que lea 3 datos de entrada que corresponden a las dimensiones de
los lados de un triángulo. A continuación debe determinar e informar qué tipo de triángulo
es, teniendo en cuenta los siguiente:
- Si se cumple Pitágoras entonces es triángulo rectángulo
- Si sólo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a = float(input("ingresa el lado A"))
b = float(input("ingresa el lado B")) 
c = float(input("ingresa el lado C"))

if c**2 == a**2 + b**2:
    print("Es un triangulo rectàngulo")
if  a != b != c:
    print ("es un triangulo escaleno")
if (a == b and c != a) or (b == c and a != b) or (a==c and c != b):
    print("es uun triangulo isòsceles")

elif a == b == c :
    print("es equilatero")


Programación 2024/25
IES Jacarandá Brenes
17. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo).

num1 = float(input("dime un numero: "))
num2 = float(input("dime un numero: "))

if num1 >= num2 :
    distancia = num1 - num2
    print(f"La distancia es entre {num1} y {num2} es : {distancia}")
else:
    distancia = num2 - num1
    print(f"La distancia es entre {num1} y {num2} es : {distancia}")


18. El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95
euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar
el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía
de autobuses y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("digite la cantidad de alumno que van a viajar: "))


if 0 < alumnos < 30 :
    totalPago = 4000/alumnos
    print ("el total a pagar a la compañía de autobuses es de: 4000 euros y cada alumno debe pagar: ", totalPago, "euros")
elif 30 <= alumnos <=49:
    totalPago = alumnos * 95 
    print ("el total a pagar a la compañía de autobuses es de:", totalPago, "euros y cada alumno debe pagar 95 euros")
elif 50 <= alumnos <=99:
    totalPago = alumnos * 70 
    print ("el total a pagar a la compañía de autobuses es de:", totalPago, "euros y cada alumno debe pagar 70 euros")
elif alumnos >= 100:
    totalPago = alumnos * 65
    print ("el total a pagar a la compañía de autobuses es de:", totalPago, "euros y cada alumno debe pagar 65 euros")
else:
    print("la cantidad digitada es cero o no se puede calcular")


19. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el
cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1
euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y
si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo
para determinar cuánto debe pagar por cada concepto una persona que realiza una
llamada. """
"""



"""

