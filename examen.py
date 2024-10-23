tamaño_empresa = int(input("Dime el tamaño de la empresa: "))
while tamaño_empresa <= 0:
    tamaño_empresa = int(input("Tamaño incorrecto, dime el tamaño de la empresa correctamente: "))

h = 0
m = 0
python = 0
java = 0
edad_total = 0

for i in range(tamaño_empresa):
    edad = int(input("Dime la edad: "))
    while edad <= 0:
        edad = int(input("Edad incorrecta, dime una edad correcta: "))
    edad_total += edad

    sexo = input("¿Qué sexo eres, H para hombre, M para mujer?: ").lower()
    while sexo != "h" and sexo != "m":
        sexo = input("Letra incorrecta: ¿Qué sexo eres, H para hombre, M para mujer?: ").lower()

    if sexo == "h":
        h += 1
    elif sexo == "m":
        m += 1

    lenguaje = input("Dime qué lenguaje usas (python o java): ").lower()
    while lenguaje != "python" and lenguaje != "java":
        lenguaje = input("Lenguaje erróneo, dime qué lenguaje usas: ").lower()
  
    if lenguaje == "python":
        python += 1
    elif lenguaje == "java":
        java += 1

print(f"El {python/tamaño_empresa*100}% de empleados utiliza Python, de los que {h} son hombres y {m} son mujeres, y su edad media es {edad_total/tamaño_empresa}")
print(f"El {java/tamaño_empresa*100}% de empleados utiliza Java, de los que {h} son hombres y {m} son mujeres, y su edad media es {edad_total/tamaño_empresa}")



