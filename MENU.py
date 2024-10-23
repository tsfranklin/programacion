MENU = """# MENU
       #1. Ingresar dinero
       #2. Retirar dinero
       #3. Consultar saldo
       #4. Salir """

print(MENU)

opcion_seleccionar = 0
dinero_en_cuenta = 0
historico = ""
ingresos, retiradas = 0, 0

while opcion_seleccionar != 4 :

    opcion_seleccionar = int(input("que opcion quiere seleccionar: "))
    
    if opcion_seleccionar == 1: #ingresar efectivo
        cantidad_ingresar = int(input("¿que cantidad desea ingresar?"))
        
        while cantidad_ingresar <0:
            cantidad_ingresar = int(input("introduzca una cantidad validad, ¿que cantidad desea ingresar?:"))
            
        dinero_en_cuenta+=cantidad_ingresar
        ingresos+=1

        historico+= f"Operacion {ingresos + retiradas}: Ingreso realizado por valor de {cantidad_ingresar}. Total: {dinero_en_cuenta}\n "

    elif opcion_seleccionar == 2: #retirar efectivo
        cantidad_retirar = int(input("que cantidad desea retirar: "))

        while cantidad_retirar > dinero_en_cuenta or cantidad_retirar < 0:
            cantidad_retirar = int(input("introduzca una cantidad validad, que cantidad desea retirar: "))
        
        dinero_en_cuenta-= cantidad_retirar
        retiradas+=1
        historico+= f"Operacion {ingresos + retiradas}: Ingreso realizado por valor de {cantidad_ingresar}. Total: {dinero_en_cuenta}\n "

    elif opcion_seleccionar ==3:
        print(f"Dispone de un saldo en la cuenta de {dinero_en_cuenta}")

print (f"se ha efectuado{ingresos} operaciones de ingresos y {retiradas} operaciones de retirada")
print(historico)




