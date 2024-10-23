"""3. Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva cuántos
días han transcurrido desde el 1 de enero de ese mismo año (considera que puede
tratarse de un año bisiesto).

dia = 2
mes = 6
año = 2024

#año = int(input("Diga el año: "))

enero = 31
febrero = 59
marzo = 90
abril = 120
mayo = 151
junio = 181
julio = 212
agosto = 243
septiembre = 273
octubre = 304
noviembre = 334
diciembre = 365


if ((año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)):
  if (dia == 29 and mes ==2):
    diasTranscurrido = febrero + 1
  elif mes == 3:
    diasTranscurrido = febrero + dia + 1
  elif mes == 4:
    diasTranscurrido = marzo + dia + 1
  elif mes == 5:
    diasTranscurrido = abril + dia + 1
  elif mes == 6:
    diasTranscurrido = mayo + dia  + 1
  elif mes == 7:
    diasTranscurrido = junio + dia  + 1
  elif mes == 8:
    diasTranscurrido = julio + dia  + 1
  elif mes == 9:
    diasTranscurrido = agosto + dia  + 1
  elif mes == 10:
    diasTranscurrido = septiembre + dia  + 1
  elif mes == 11:
    diasTranscurrido = octubre + dia  + 1
  elif mes == 12:
    diasTranscurrido = noviembre + dia  + 1
  
elif mes == 1 :
    diasTranscurrido = dia
elif mes == 2:
    diasTranscurrido = enero + dia
elif mes == 3:
    diasTranscurrido = febrero + dia
elif mes == 4:
    diasTranscurrido = marzo + dia
elif mes == 5:
    diasTranscurrido = abril + dia
elif mes == 6:
    diasTranscurrido = mayo + dia
elif mes == 7:
    diasTranscurrido = junio + dia
elif mes == 8:
    diasTranscurrido = julio + dia
elif mes == 9:
    diasTranscurrido = agosto + dia
elif mes == 10:
    diasTranscurrido = septiembre + dia
elif mes == 11:
    diasTranscurrido = octubre + dia
elif mes == 12:
    diasTranscurrido = noviembre + dia
  
print (diasTranscurrido)


Un hotel ofrece dos tipos de habitaciones: estudios y apartamentos.Crea un programa
que calcule el precio del total de la estancia en el hotel para estudios y apartamentos
dependiendo del mes y tiempo de estancia teniendo en cuenta los siguientes precios y
los descuentos aplicables:
Mayo y Octubre Junio y Septiembre Julio y Agosto
Estudio– 50€/Noche Estudio– 75.20€/Noche Estudio– 76€/Noche
Apartamento 76€/Noche Apartamento 63.70€/Noche Apartamento 80€/Noche
La tarifa para el resto del año es de 40€/noche para estudios y 55€/noche para
apartamentos.
Descuentos aplicables:
● Para estancias de más de 10 noches en un estudio durante los meses de mayo y
octubre se aplica un descuento del 5%.
● Para estancias de más de 20 noches en un estudio durante los meses de mayo y
octubre se aplica un descuento del 25%.
● Para estancias de más de 12 noches en un estudio durante los meses de junio y
septiembre se aplica un descuento del 20%.
● Para estancias de más de 10 noches en un apartamento cualquier mes del año se
aplica un descuento del 10%.

tipo = input("que tipo de habitacion desea estudio o apartamento? :  ").lower
fecha = input("digite el mes de la estadia: ")
noche=int(input("digiete la cantidad de noche: "))

while noche < 0:
  noche = int(input("digiete la cantidad de noche: "))

if fecha == "mayo" or fecha == "octubre":
  if tipo == "estudio" :
    if 0 <= noche <= 10 :
     total = 50 * noche 
    elif 10 < noche <=20 :
     total = 50 * noche * .95
    else:
      total = 50 * noche * .75
  else: 
    if 0 <= noche <= 10 :
      total = 76 * noche
    else:
      total = 76 * noche * .90

      
elif fecha == "junio" or  fecha=="septiembre":
  if tipo == "estudio":
     if 0 <= noche <= 12 :
       total = 75.2 * noche
     elif noche > 12 : 
       total = 75.2 * noche * .80
  else: 
    if 0 <= noche <= 10 :
      total = 63.7 * noche
    else:
      total = 63.7 * noche * .90

elif fecha == "julio" or  fecha =="agosto":
   if tipo == "estudio"  and noche >= 0:
      total = 76 * noche
   elif tipo == "apartamento" and 0 <= noche <= 10:
      total = 80 * noche
   else: 
     total = 80 * noche * .90

elif fecha == "enero" or fecha == "febrero" or fecha == "marzo" or fecha == "abril" or fecha == "noviembre" or fecha == "diciembre": 
    if tipo == "estudio" and noche >= 0 :
      total = 40 * noche
    elif tipo == "apartamento" and 0 <= noche <= 10:
      total = 55 * noche
    else :
      total = 55 * noche * .90

else:
  print("vuelva a ingresar los datos algunos son incorrectos")


print ("estotal a pagar es: ", total)

5. Crea un programa que reciba las coordenadas de un rectángulo ({x1, y1} y {x2, y2})y
de un punto (x, y)y determine si el punto se encuentra dentro del rectángulo(True) o
fuera de éste (False). Considera que siempre se cumple x1>x2 y1>y2"""

x1 = 2
y1 = 2

x2 = -3
y2 = -1


x3 = -1
y3 = 1


if x1 > x3 and y3 < y1 and x2 < x3 and y2 < y3:
   print(f"cordenada{x3, y3} dentro ")
else:
  print(f"cordenada{x3, y3} fuera o en la linea ")

  










    
