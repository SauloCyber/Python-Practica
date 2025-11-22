# Hola, Bienvenido a mi pequeño programa para calcular promedios

maximointentos = 3
intentos = 0

print("""Hola, Este es un programa simple para 
calcular el promedio de tus notas
      """)

while True:
    print("""Que tipo de promedio quieres saber?
1. Promedio de un año escolar. (Ej: "el promedio que obtuve en 3ro de la Secundaria".)
2. Promedio mas usado. desde 3ro hasta 6to de la secundaria.
3. Salir""")

    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        cantidad = int(input("Cuantas materias son en total?: "))
        suma = 0
        for i in range(1, cantidad + 1):
            nota = float(input(f"Introduce la nota de la materia {i}: "))
            suma += nota 

        promedio = suma / cantidad
        print("Tu promedio es: ", promedio)

    elif opcion == 2:
        promedio1 = int(input("Introduce el promedio que obtuviste en 3ro de Secundaria: "))
        promedio2 = int(input("Introduce el promedio que obtuviste en 4to de Secundaria: "))
        promedio3 = int(input("Introduce el promedio que obtuviste en 6to de Secundaria: "))
    
        promediototal = promedio1+promedio2+promedio3
        total = promediototal/3
        print("Tu promedio es: ", total)

    elif opcion == 3:
        print("Gracias por usar mi pequeño programa")
        break

    else:
        intentos += 1
        print("opcion invalida. Por favor introdusca una opcion vlaida. Intentos: ", intentos)
        
        if intentos == maximointentos:
            print("Lo siento has alcanzado el limite de intentos fallidos.")
            exit()
        

    



