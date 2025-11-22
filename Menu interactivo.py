inicio = input("Hola Bienvenido a mi programa escribe 'empezar' si quieres entrar: ")
while inicio == 'empezar':

    print("""Hola, bienvenido a mi programa ¿qué quieres hacer?
    1. Mostrar un número al azar entre 1 y 100
    2. Elevar un número a una potencia
    3. Calcular el promedio de 3 números
    4. Ver si un número es par o impar
    5. Salir del programa""")

    opcion = input("Elige una opcion: ")

    if opcion == '1':
        import random
        numero = random.randint(1, 100)
        print(numero)

    elif opcion == '2':
        n1 = int(input("Ingresa el primer numero ENTERO: "))
        n2 = int(input("Ingresa el segundo numero ENTERO: "))
        print("Tu numero al azar es: ", n1**n2)

    elif opcion == '3':
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        n3 = int(input("Ingrese el tercer numero: "))
        print("El promedio es: ", (n1+n2+n3) / 3)
    
    elif opcion == '4':
        numero = int(input("Ingrese un numero: "))
        if numero % 2 == 0:
            print("El numero: ", numero, "es par")
        else:
            print("el numero: ", numero, "es impar")
      
    elif opcion == '5':
        volver = input("¿Estas seguro de que quieres salir? (si/no): ").lower()
        if volver != "no":
            print("Saliendo del programa.....")
            break
        
    else:
        print("Opcion Invalida")

    volver = input("¿Quieres volver al menú? (si/no): ").lower() 
    if volver != "si": 
        print("Saliendo del programa...") 
        break






