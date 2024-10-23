"""Write a program in python to display the sum of the series [ 9 + 99 + 999 + 9999 ...]
given a number of terms.
- Input the number or terms :5
- Expected Output: 9 99 999 9999 99999. The sum of the series = 111105

n = 100
suma = 0
Numero_repetido = 9

for i in range ( 1, n+1):

    conversion=str(Numero_repetido)*i
    suma += int(conversion)

print(suma)

#2. Escriba un programa para imprimir el Triángulo de Floyd con dos opciones: basado en binario o triángulos de base decimal.

piramide = 10
impar=""
par =""

for i in range(1,piramide+1):
    if i % 2 == 0 :
        for x in range (1,i+1):  
            if x % 2 == 0:
                par+="1"
            else:
                par+="0"    
        print(par)            
    elif i % 2 !=0:
        for x in range (1,i+1):
            if x % 2 == 0:
                impar+="0"
            else:
                impar+="1"    
        print(impar)
    impar=""   
    par=



piramide = 10
contador = 0
par = ""
impar = ""

for i in range(1,piramide+1):
    if i % 2 == 0 :
        for x in range (1,i+1):  
            if x % 2 == 0:
                contador+=1
                par+=str(contador)+" "
            elif x % 2 !=0:
                contador+=1 
                par+=str(contador)+" "
        print(par) 
        par=""           
    elif i % 2 !=0:
        for x in range (1,i+1):
            if x % 2 == 0:
                contador+=1
                impar+=str(contador)+" "
            elif x % 2 !=0:
                contador+=1 
                impar+=str(contador)+" "
        print(impar) 
        impar=

3. Write a program to find the sum of the series [ x - x3 + x5 +... + xn] for a given number of terms     

x = 2

n = 5
total = 0
lista = []
contador = 1

for i in range(1,n+1):
    if i % 2 != 0 :
        subtotal = x**contador
        total+=subtotal
        lista.append(subtotal)
        contador+=2
        
    else:
        subtotal=x**contador
        total-=subtotal
        lista.append(-subtotal)
        contador+=2
print(lista, "=", total)        


5. Diseña un programa que pida dos números enteros y nos muestre los siguientes
diez números que son múltiplos del segundo introducido a partir del primero. Por
ejemplo, si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
(a partir de 13 los siguientes 10 múltiplos de 7)


inicio = 13
multiplo = 7 
contador = 0

while contador < 10:
    inicio+=1
    if inicio % multiplo == 0:
        print(inicio)
        contador+=1

6. La secuencia siguiente está definida para el conjunto de los números enteros:
n → n/2 (n es par)
n → 3n + 1 (n es impar)
Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
de números:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

n=int(input("el número introducido no es correcto, ingrese un número mayor que cero"))
lista=[]


while n <=0:
    n=int(input("el número introducido no es correcto, ingrese un número mayor que cero"))
while n != 1 :

    if n % 2 ==0:
       nx= n/2
       lista.append(nx)
       
    elif n % 2 != 0:
        nx= 3*n + 1
        lista.append(nx)

    n=nx
print(lista)    


7. Diseña un algoritmo en el que a partir de una fecha introducida por teclado con
formato día, mes, año se obtenga la fecha del día siguiente. El programa debe
terminar cuando la fecha introducida no sea válida (por ejemplo, 30-02-2024).


def es_fecha_valida(dia, mes, año):
    return ((dia >= 1 and dia <=30) and (mes==4 or mes ==6 or mes==9 or mes ==11) and año>=1) or ((dia >= 1 and dia <=31) and (mes==1 or mes ==3 or mes == 5 or mes==7 or mes ==8 or mes ==10 or mes==12) and año>=1) or (dia>=1 and dia<=28 and mes==2 and not((año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)) and año>=1 ) or (dia>=1 and dia<=29 and mes==2 and ((año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)) and año>=1 )

dia=int(input("introduzca el dia: "))
mes=int(input("introduzca el mes: "))
año=int(input("introduzca el año: "))

while es_fecha_valida(dia, mes, año) == True:
    #evalua si es el ultmo dia del mes, si lo es se le suma 1 al mes y el dia quedaria en 1 con el mismo año
   if (dia == 30 and (mes ==4 or mes ==6 or mes==9 or mes ==11)) or (dia==31 and (mes==1 or mes ==3 or mes == 5 or mes==7 or mes ==8 or mes ==10 or mes==12)) or (dia==29  and mes==2) or (dia==28 and mes==2):
       mes+=1
       dia=1
   elif dia==31 and mes==12:
       año+=1
       mes=1
       dia=1
   else:
       dia+=1
   print(dia, mes, año)

   dia=int(input("introduzca el dia: "))
   mes=int(input("introduzca el mes: "))
   año=int(input("introduzca el año: "))

print("fecha invalida a terminado el programa")


8. Crea un programa que reciba un número entero positivo mayor que cero y devuelva
una secuencia de Fibonacci de longitud igual a este valor.
La sucesión de Fibonacci es una sucesión numérica en la que cada término es igual
a la suma de los dos anteriores, salvo los dos primeros que se toman como 1 y 1.
Así, una sucesión de longitud nueve sería: 1, 1, 2, 3, 5, 8, 13, 21, 34

longitudFIbonacci = 9
fibonacci1 = 0
fibonacci2 = 1
print(1)

for i in range( longitudFIbonacci-1):
    total= fibonacci1 + fibonacci2
    print(total) 
    fibonacci1=fibonacci2
    fibonacci2= total


9. Se considera la serie definida por: a1=0, a2=1, an=3*an-1+2*an-2
(n≥3) Se desea crear
un programa que calcule el valor y el rango (subíndice) del primer término que sea
mayor o igual a 1000."""

n1=0
n2=1
resultado=0
contador=2
while resultado <=1000 :
    resultado= 3*n2 + 2*n1
    n1=n2
    n2=resultado
    contador+=1
    print(resultado)





"""10. Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es impar su familia le regala un puzzle; si es par, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.

edad=8
acumulaDinero= 20
recibeDinero=20
acumulaPuzzle=1
recibepuzzle=1
print(1)
print(20)

for i in range(1,edad-1):
   
    if i % 2 == 0:
        recibeDinero=recibeDinero+15
        acumulaDinero+=recibeDinero
        print(acumulaDinero)
    else: 
        recibepuzzle=recibepuzzle*2
        acumulaPuzzle+=recibepuzzle
        print(acumulaPuzzle)
        
print(f"hasta la {edad} a recibido {acumulaDinero} dinero y {acumulaPuzzle} puzzle")




11. Crea un programa que reciba el nombre de una figura geométrica y la longitud del
lado de ésta y genere una figura vacía como las siguientes. Incluye la posibilidad de
que se cambie el símbolo utilizado para pintar la figura
    


figura="cuadrado"
longitud=4

for i in range(1,longitud+1):
    if i==1:
        lado=longitud*"* "
        print(lado)
    elif i < longitud and i>1 :
        lado="*"+(" "*(longitud+1))+"*"
        print(lado)
    elif i==longitud:
        lado=longitud*"* "
        print(lado)

figura="cuadrado"
longitud=4

for i in range(longitud+1):
    if i==0:
        lado=(longitud)*" "+"  *"
        print(lado)
    elif i>0 and i<(longitud-1):
        lado=(longitud-i)*" "+"* "+((" "*(i*2)))+" *"
        print(lado)
    elif i==longitud:
       lado=longitud*" * "
       print(lado)"""
     








    






    

    
    
