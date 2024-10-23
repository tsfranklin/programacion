

#1. Escribe un programa que reciba dos números por teclado y que después muestre
#por pantalla los números que hay entre ellos. Por ejemplo, si se recibe 5 y 3 se
#mostrará: 3, 4, 5. Utiliza bucle for y while [for/while].


# con for


"""num1= int(input("introduzca un numero: "))
num2= int(input("introduzca otro numero: "))


if num1 > num2:
   for num2 in range (num2, num1+1):
       print (num2)
       num2+=1
elif num2 > num1:
   for num1 in range (num1, num2+1):
       print (num1)
       num1+=1
else:
   print("los numeros som imguales")




# con while




if num1 > num2:
  num2=num2
  while num2 <= num1:
       print (num2)
       num2=1+num2
elif num2 > num1:
  num1 = num1
  while num1 <= num2:
       print (num1)
       num1=1+num1
else:
   print("los numeros som imguales")




#Crea un programa que reciba un número y a continuación muestre la tabla de
#multiplicar de ese número. Utiliza sólo bucles de tipo while.


num = 5
i=0


while i <= 10:
   resultado = i * num
   i+=1
   print(f"{i}x{num}={resultado}")


# Escribe un programa que reciba dos números y muestre por pantalla todos los
#números que hay en ese intervalo que son múltiplos de 7 [for/while].


num1= int(input("introduzca un numero: "))
num2= int(input("introduzca otro numero: "))
multiplos7 = []




if num1 > num2:
  num2=num2
  while num2 <= num1:
       if num2 % 7 ==0:
          
           multiplos7.append(num2)
       num2=1+num2
elif num2 > num1:
  num1 = num1
  while num1 <= num2:
      if num1 % 7 ==0:
         
          multiplos7.append(num1)
      num1=1+num1
else:
   print("los numeros som imguales")
   if num1 % 7 ==0:
       multiplos7.append(num1)
       print(f"y {multiplos7} es multiplo de")




print(multiplos7)




#4. Crea un programa que reciba números hasta que se introduzca uno fuera del rango
#0 - 10.000. En ese momento informará de cuántos números se han introducido y la media de éstos.
#"Se han introducido 50 números y la media es de 3.28.


num = int(input("introduzca numero entre 0 y 10.000 Presione un numero fuera del rango para salir: "))

contador = []
suma = 0

if num < 0 and num > 10000:
   print("el numero ingresado esta fuera del rango no se puede continuar")
else:
   while num >= 0 and num <= 10000:
     contador.append(num)
     suma +=num
     num=int(input("introduzca numero entre 0 y 10.000 presione un numero fuera del rango para salir: "))
    
   if len(contador) > 0:
     print(f"El promedio de {contador} / {len(contador)} = {suma / len(contador)}")
   else:
     print("No se ingresaron números dentro del rango.")

print("fin del programa")


5. Escribe un programa que reciba un número n entero positivo y devuelva la suma de
los números existentes entre 1 y n. Si el número no es un entero positivo debe
informar del error y solicitarlo de nuevo.


numero = 5.0

total=0

while numero <= 0 or type(numero)!= int:
   numero=(print("introduzca un numero entero positivo"))

for i in range(1,numero+1):
 total= i + total
print(total)


#6. Crea un programa similar al anterior, pero que reciba dos números enteros positivos
#n, m y devuelva la suma de los números entre n y m. Valida los dato


num1= int(input("introduzca un numero: "))
num2= int(input("introduzca otro numero: "))
total = 0

if num1 > num2:
   for num2 in range (num2, num1+1):
       print (num2)
       total+= num2
       num2+=1
   print("el total es: ", total)
elif num2 > num1:
   for num1 in range (num1, num2+1):
       print (num1)
       total+=num1
       num1+=1
   print("el total es: ", total)
else:
   print("los numeros som imguales")


7. Se desea crear un programa que lea desde teclado una serie de números hasta que
aparezca alguno menor que 1000. Cuando esto ocurra deberá mostrar cuál ha sido
el número más grande que se ha introducido.


numero = int(input("introduzca numeros, para salir del programa debes introducir un numero menor que 1000: "))
numeroMayor=0


while numero >= 1000:
      if numero > numeroMayor:
        numeroMayor=numero
      else:
        print("el numero mayor sigue siendo", numeroMayor)
      numero = int(input("introduzca numeros, para salir del programa debes introducir un numero menor que 1000: "))
print("el numero mayor es: ", numeroMayor)


8. Crea un programa que reciba dos números num_1 y num_2 y devuelva el producto
de ambos, pero sin utilizar el operador de la multiplicación (*). Los números pueden
ser enteros positivos/negativos.

num_1 = int(input("introduzca un numero "))
num_2 = int(input("introduzca un numero "))
resultado = 0


if num_1 < 0 : #cuando los dos numeros son negativos and num_2 <0
   for i in range(-num_1):
      resultado-=num_2
   print(resultado)
else:
   for i in range(num_1):
      resultado+=num_2
   print(resultado)

9. Diseña un programa que realice la operación módulo (%) de dos números, sin
utilizar esta operación ni la división.


num1 = 100
num2 = 4
contador = 0
vueltas = 0
restofinal = 0


if num1 == num2:
   print(0)
elif num1 > num2:
   for i in range (1,num1*2,num2):
      contador+=num2
      vueltas+=1
      if contador == num1:
         print(0)
      elif contador > num1 :
         vueltas-=1
         resto = (num1-num2 * vueltas) 
#         contador = 0
#        vueltas = 0
#         for i in range (1,resto*2,num2):
#           contador+=num2
#            vueltas+=1
#            if contador ==resto:
#              print(0)
#           elif contador > resto :
#               vueltas-=1
#              restofinal = resto - num2 * vueltas 
print (resto)  
print(num1%num2)       
          

10. Escribe un programa que pida al usuario cuántos números positivos quiere introducir
para a continuación pedirlos por consola. Si el usuario introduce un número erróneo
volverá a pedirlo y una vez que se hayan introducido todos mostrará la media, cuál
es el mayor y cuál el menor.

cantidadNumero = int(input("cuantos numeros vas a ingresar: "))
pedirNumeros = []
mayor=0
menor=0
suma=0
contador =0

if cantidadNumero <= 0:
   print("fin del programa  con la cantidad introducida no se puede operar")

else:

   for i in range (cantidadNumero):
      numeros=int(input("intraduzca un numero positivo: "))
      while numeros <= 0:
         numeros=int(input("el numero introducido no es un numero positivo. Intraduzca un numero positivo: "))

      pedirNumeros.append(numeros)
      contador+=1
      suma+=numeros
      menor = numeros
      mayor = numeros


   for i in range (0,len(pedirNumeros)):
      for x in range (0,len(pedirNumeros)):
         if pedirNumeros[i] >= pedirNumeros[x] and pedirNumeros[i] >= mayor :
            mayor=pedirNumeros[i]
         elif pedirNumeros[i] <= menor:
            menor=pedirNumeros[i]

   print(f"el numero mayor es: {mayor}, el numero menor es: {menor}, el promedio es {suma/cantidadNumero}")

11. Escribe un programa que reciba un valor y cree una pirámide de asteriscos de altura
ese valor (cada línea contiene un número impar de asteriscos). Por ejemplo, para
valor = 3 tendríamos:

piramide = 10

for i in range(1,piramide+1):
    print((piramide-i)*" ", (i*2-1)*"*")

12. Crea un programa que reciba un entero positivo mayor que 0 y a continuación
informe si es un número perfecto. Un número es perfecto si es igual a la suma de
todos sus divisores.



numero_perfecto = 6
divisores = []
suma = 0
for i in range(1,numero_perfecto):
   if numero_perfecto % i == 0:
      divisores.append(i)
      suma+=i

if suma == numero_perfecto:
   print("es un numero perfecto")
else: 
   print("no es un numero perfecto")


13. Write a program in C to display the n terms of a harmonic series and their sum.
Harmonic series contains 1/1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms.
- Input the number of terms : 5
- Expected Output : 1/1 + 1/2 + 1/3 + 1/4 + 1/5:
- Sum of Series up to 5 terms : 2.283334 

serie = -5
resultado = 0
for i in range (1,serie+1):
   print(f"1/{i}")
   resultado+= 1/i

print (resultado)

print(1/-1 + 1/-2 + 1/-3 + 1/-4 + 1/-5)


14. Write a program in python to display a pattern like a diamond.

piramide = 10

for i in range(1,piramide+1):
    print((piramide-i)*" ", (i*2-1)*"*")
for i in range(piramide-1,0, -1):
    print((piramide-i)*" ", (i*2-1)*"*")




15. Given the number n (n >=0), write a program to find its factorial. Factorial of n is
defined as 1 x 2 x … x n. For n = 0, factorial is 1."""

factorial = 0
resultado=1

for i in range (1,factorial+1):
   resultado*=i
print(resultado)















