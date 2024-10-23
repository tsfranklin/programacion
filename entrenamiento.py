MENU = """Amazon Jacaranda
        A) Añadir cliente
        B) Mostrar los % premium y normales
        G) Salir  """

clienteRegular=[]
premium=[]
CorreoPremium=[]
CorreoRegular=[]
comparadorPrecioPremium = 0
codigoproductovendidoCostosoPremium =[]
importeMaximoPremium = 0
comparadorPrecioRegular = 0
codigoproductovendidoCostosoRegular =[]
importeMaximoRegular = 0
print(MENU)
opcion = str(input("elije una opcion, para salir preciona g: ")).lower()
while opcion != "g":
    if opcion == "a":
        cliente = str(input("ingrese el nombre del cliente:"))
        aceptaNoacepta = str(input("preciones un (S) si quiere ser cliente premium o (N) para ser regular:")).lower()
        correos = str(input("introduzca su correo electronico: "))
        
        llevaProducto = str(input("lleva productos (S) para si (N) para no: "))  
        if aceptaNoacepta == "s":
            premium.append(cliente)

            if llevaProducto == "s":
                codigoProducto = input("introduzca el codigo del producto: ")
                unidades= int(input("diga cuantas unidades: "))
                precioUnitario= float(input("introduzca el precio unitario del producto"))
                importeMaximo = unidades * precioUnitario
                if precioUnitario >=comparadorPrecioPremium:
                    comparadorPrecioPremium=precioUnitario
                    codigoproductovendidoCostosoPremium.append(codigoProducto)
                if importeMaximo > importeMaximoPremium:
                    importeMaximoPremium=importeMaximo
                    CorreoPremium.append(correos)

        elif aceptaNoacepta == "n":
            clienteRegular.append(cliente)
            if llevaProducto == "s":
                codigoProducto = input("introduzca el codigo del producto: ")
                unidades= int(input("diga cuantas unidades: "))
                precioUnitario= float(input("introduzca el precio unitario del producto"))
                importeMaximo = unidades * precioUnitario
                if precioUnitario >=comparadorPrecioRegular:
                    comparadorPrecioRegular=precioUnitario
                    codigoproductovendidoCostosoRegular.append(codigoProducto)
                if importeMaximo > importeMaximoRegular:
                    importeMaximoRegular=importeMaximo
                    CorreoRegular.append(correos)


        opcion = str(input("elije una opcion, para salir preciona g: ")).lower()
    elif opcion=="b":
        if len(premium) + len(clienteRegular) == 0:
            print("no existen datos")
        else:
            print(f"el % de premium es : {(len(premium)/(len(premium)+len(clienteRegular)))*100}\
                   el % de normales es: {(len(clienteRegular)/(len(premium)+len(clienteRegular)))*100} ")

    elif opcion == "c":
        print (f"el % de premium es : {(len(premium)/(len(premium)+len(clienteRegular)))*100}")
        print (f"el importe maxio es de: {importeMaximoPremium} del correo {CorreoPremium}")
        print (f"el codigo del producto mas costoso es: {codigoproductovendidoCostosoPremium} con precio de : {comparadorPrecioPremium} ")
    
    elif opcion =="d":
        print (f"el % de premium es : {(len(clienteRegular)/(len(premium)+len(clienteRegular)))*100}")
        print (f"el importe maxio es de: {importeMaximoRegular} del correo {CorreoRegular}")
        print (f"el codigo del producto mas costoso es: {codigoproductovendidoCostosoRegular} con precio de : {comparadorPrecioRegular} ")

    elif opcion =="e":
        if importeMaximoPremium > importeMaximoRegular:
            print(CorreoPremium)
            print(importeMaximoPremium)
        elif importeMaximoRegular > importeMaximoPremium:
             print(CorreoRegular)
             print(importeMaximoRegular)
        else:
            print(CorreoPremium)
            print(importeMaximoPremium)
            print("y")
            print(CorreoRegular)
            print(importeMaximoRegular)
            print("son nustros maximos clientes")





    opcion = str(input("elije una opcion, para salir preciona g: ")).lower()
print("fin del programa")
        

        
