Maximointentos = 3
intentos = 0
Token = False
Estudiantes = {
    "Juan": False,
    "Marcos": False,
    "María": False,
    "Luis": False,
    "Camila": False,
    "Andrés": False,
    "Sofía": False,
    "Pedro": False,
    "Ana": False,
    "Carlos": False,
    "Valeria": False,
    "Diego": False,
    "Lucía": False,
    "Fernando": False,
    "Isabela": False,
    "Javier": False,
    "Gabriela": False,
    "Ricardo": False,
    "Paula": False,
    "Martín": False
}

while True:
    pin = str(input("Bienvenido Profesor Ricky Martinez. Por favor introduzca su PIN: "))
    if pin == '1590':
        Token = True
        print("Hola Profesor Ricky Martinez")
        break

    else:
        intentos +=1
        print("Pin invalido. Intentos: ", intentos)

    if intentos >= Maximointentos:
        print("Demasiados intentos. ACCESO BLOQUEADO")
        exit()

while True:
    if Token == True:
        print("""Que quieres hacer?
                1. Anotar asistencia
                2. Ver Asistencia
                3. Salir""")
        
        option = int(input("Introduce una opcion: "))

        
        if option == 1:
            while True:
                presente = str(input("Quien esta presente?: "))

                if presente.lower() == 'salir':
                    break
                
                if presente in Estudiantes:
                    if Estudiantes[presente]:
                     print(f"{presente} Estudiante estaba marcado como presente")

                    else:
                        Estudiantes[presente] = True
                        print(f"{presente} ha sido marcado como presente.  Si desea regresar al menu principal escriba 'Salir'")
                        
                else:
                    print("Estudiante no encontrado")
                
        
        elif option == 2:
            print("Asistencia de estudiantes")
            for nommbre, presente in Estudiantes.items():
                    estado = "Presente" if presente else "Ausente"
                    print(f"- {nommbre}: {estado}")
                        
            while True:
                    respuesta = input("¿Desea volver al menú? (si/no): ").lower()
                    if respuesta == "si":
                        break  
                    elif respuesta == "no":
                        print("Gracias por usar el sistema de asistencia.")
                        exit()
                    else:
                         print("Respuesta inválida. Escribe 'si' o 'no'.")

        elif option == 3:
            print("Gracias por usar nuestro programa. Que tenga un Buen Dia profesor")
            exit()
        
        else:

            print("Opcion no valida")
