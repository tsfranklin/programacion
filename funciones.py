
"""def es_mayor_edad (edad):
    return edad > 18
print(es_mayor_edad(20)) 



#esto es lo mismo que esto, las funciones solo deben calcular una sola cosa, y reciben lo que sea un str un int cadena etc.
edad= 20

if edad > 18:
    resultado = True
else:
    resultado= False
print(resultado)




def saludar (name, surname, age=18 ):
    return f"minombre es {name} {surname} y tengo {age} años"
print(saludar("julieta", "gomes", 28))
print( saludar(surname="torres", name="franklin", age=18))
print()

def es_año_bisiesto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

print(es_año_bisiesto(100))


#diseño dirigido por test


def multiplicacion (x, y):
    return x * y

assert (multiplicacion(2,2)==4)
assert (multiplicacion(0,2)==0)
assert (multiplicacion(-2,2)==-4)
assert (multiplicacion(-2,-2)==4)
Enero 31 Marzo 31 Abril 30 Mayo 31 Junio 30 Julio 31 Agosto 31 Septiembre 30 Octubre 31 Noviembre 30 Diciembre 31"""


def es_fecha_valida(dia, mes, ano):
    return ((dia >= 1 and dia <=30) and (mes==4 or mes ==6 or mes==9 or mes ==11) and ano>=1)\
          or ((dia >= 1 and dia <=31) and (mes==1 or mes ==3 or mes == 5 or mes==7 or mes ==8 or mes ==10 or mes==12) and ano>=1)\
          or (dia>=1 and dia<=28 and mes==2 and not((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)) and ano>=1 ) \
          or (dia>=1 and dia<=29 and mes==2 and ((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)) and ano>=1 )

assert (es_fecha_valida(1,1,2024)==True)
assert (es_fecha_valida(29,2,2024)==True)
assert (es_fecha_valida(28,2,2023)==True)
assert (es_fecha_valida(30,2,2024)==False)
assert (es_fecha_valida(31,4,2024)==False)
assert (es_fecha_valida(0,12,2024)==False)
assert (es_fecha_valida(1,12,0)==False)
assert (es_fecha_valida(1,13,2024)==False)
assert (es_fecha_valida(32,3,2024)==False)


#test driven development---TDD or DDT














