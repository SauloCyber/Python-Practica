""" Bienvenidos a mi programa simple, una pequeña Biblioteca de estudiantes 
    del ITLA, donde pueden: Tomar un libro prestado, ver libros disponibles y 
    buscar un libro por su nombre.
"""
# Aqui definimos las variables a utilizar
Maximodeintentos = 3
intentos = 0
Login = False
Token = False

# aqui creo un pequeño diccionario con los nombres de los estudiantes, su matricula y carrera
Estudiantes = {
    "2025-7777": {"Nombre": "Pedro", "Carrera": "Seguridad Informatica"},
    "2025-6124": {"Nombre": "Amanda", "Carrera": "Software"},
    "2025-8741": {"Nombre": "María", "Carrera": "Mecatronica"},
    "2025-4398": {"Nombre": "Luis", "Carrera": "Inteligencia Artificial"},
    "2025-9920": {"Nombre": "Camila", "Carrera": "Ciberseguridad"},
    "2025-5513": {"Nombre": "Andrés", "Carrera": "Administración"},
    "2025-7602": {"Nombre": "Sofía", "Carrera": "Diseño Gráfico"},
    "2025-5696": {"Nombre": "Junior", "Carrera": "Desarollo de Software"},
}

# Un pequeño diccionario con libros
libros = {
    "Clean Code": {"autor": "Robert C. Martin", "disponible": True},
    "Artificial Intelligence: A Modern Approach": {"autor": "Stuart Russell y Peter Norvig", "disponible": False},
    "Introduction to Algorithms": {"autor": "Thomas H. Cormen", "disponible": True},
    "The Pragmatic Programmer": {"autor": "Andrew Hunt y David Thomas", "disponible": False},
    "Code Complete": {"autor": "Steve McConnell", "disponible": True},
    "Deep Learning": {"autor": "Ian Goodfellow, Yoshua Bengio y Aaron Courville", "disponible": False},
    "Design Patterns": {"autor": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "disponible": True},
    "Python Crash Course": {"autor": "Eric Matthes", "disponible": False},
    "You Don't Know JS": {"autor": "Kyle Simpson", "disponible": True},
    "Cracking the Coding Interview": {"autor": "Gayle Laakmann McDowell", "disponible": False},
    "Computer Networks": {"autor": "Andrew S. Tanenbaum", "disponible": True},
    "Operating System Concepts": {"autor": "Abraham Silberschatz", "disponible": False},
    "Hacking: The Art of Exploitation": {"autor": "Jon Erickson", "disponible": True},
    "The Web Application Hacker’s Handbook": {"autor": "Dafydd Stuttard y Marcus Pinto", "disponible": False},
    "Cybersecurity Essentials": {"autor": "Charles J. Brooks", "disponible": True},
    "The Phoenix Project": {"autor": "Gene Kim, Kevin Behr, George Spafford", "disponible": False},
    "Algorithms to Live By": {"autor": "Brian Christian y Tom Griffiths", "disponible": True},
    "The Mythical Man-Month": {"autor": "Frederick P. Brooks", "disponible": False},
    "Clean Architecture": {"autor": "Robert C. Martin", "disponible": True},
    "How Computers Work": {"autor": "Ron White", "disponible": False}
}

print("Bienvenido a la Biblioteca Digital del ITLA")

# Un bubcle que le pida al estudiante ingresar su matricula y si es correcta la variable Login pasa a True
while True:
    if not Login:
        matricula = str(input("Introduzca su matricula: "))
    if matricula in Estudiantes:
        Login = True
        print("Matricula Correcta")
        break
    else:
        intentos +=1                            
        print("Invalido. Intentos: ", intentos) # Un pequeño bloqueador de intentos
        if intentos >= Maximodeintentos:
            print("Demasiados intentos. ACCESO BLOQUEADO")
            exit()
# Un bucle que se incia si Login es igual a True
while True:
    if Login == True:
        nombre = str(input("Introduzca su nombre: "))

        if nombre == Estudiantes[matricula]["Nombre"]:
            print("Seccion Iniciada Correctamente. Bienvenido", nombre)
            Token = True
            break

        else:
            print("Nombre Incorrecto. Llame a soprte tecnico para solicitar ayuda.")
            intentos +=1
            print("Intentos incorrectos: ", intentos)

        if intentos >= Maximodeintentos:
            print("Demasiados intentos. ACCESO BLOQUEADO")
            exit()
    
while True:

    if Login and Token == True:
       print("""Querido Estudiante. ¿Qué desea consultar?
            1. Ver libros disponibles
            2. Prestar libro
            3. Buscar libro por nombre
            4. Salir""")
    try: 
        option = int(input("Eliga una opcion valida: "))
    except:
        print("INCORRECTO. Eliga una opcion valida")
        continue
    
    if option == 1:
        print("Libros disponibles: ")
        for titulo, datos in libros.items():
            if datos["disponible"]:
                print("-", titulo)

        while True:
            respuesta = str(input("Deseas Volver al menu anterior? (si/no): ")).lower()
            if respuesta == "si":
                break   
            elif respuesta == "no":
                print("Gracias por usar la Biblioteca digital del ITLA")
                exit()
            else:
                print("Respuesta Invalida. Por Favor Ingrese Si o No")
                break
    elif option == 2:
        busqueda = str(input("Que Libro desea?: "))

        if busqueda in libros:
            if libros[busqueda]["disponible"] == True:
                print(f"El libro '{busqueda}' esta disponible.")
                print("Autor: ", libros [busqueda]["autor"])
                print("Tus datos")
                print("Matricula: ",    matricula)
                print("Nombre: ", nombre)
                print("Carrera", Estudiantes[matricula]["Carrera"])

                while True:
                    request = str(input("Quieres proceder a tomar el libro prestado?")).lower()
                    if request == 'si':
                        print("Gracias por Utilizar nuestros servicios. " \
                        "El libro esta listo para ser retirado en la Bilioteca, Edif. 4")
                        break
                    elif respuesta == "no":
                        print("Muchas Gracias por usar nuestros serviros.")
                        break
                    else:
                        print("Respuesta inválida. Por favor ingresa 'si' o 'no'.")

            elif busqueda in libros:
                if libros[busqueda]["disponible"] == False:
                    print("El libro no se encuntra disponible")
                else:
                    print("Opcion invalida")
                    break

        while True:
            volver = str(input("Deseas Volver al menu anterior? (si/no): ")).lower()
            if volver == "si":
                break   
            elif volver == "no":
                print("Gracias por usar la Biblioteca digital del ITLA")
                exit()
            else:
                print("Respuesta Invalida. Por Favor Ingrese Si o No")
                break

    elif option == 3:
        buscar = str(input("Escriba el libro que desa buscar: "))

        if buscar in libros:
            if libros[buscar]["disponible"] == True:
                print(f"El libro '{buscar}' esta disponible.")
                print("Autor: ", libros [buscar]["autor"])
            elif libros[buscar]["disponible"] == False:
                print("el libro no se encuentra disponible")
            else:
                print("Ese libro no se encuentra en la biblioteca")

        while True:
            volver = str(input("Deseas Volver al menu anterior? (si/no): ")).lower()
            if volver == "si":
                break   
            elif volver == "no":
                print("Gracias por usar la Biblioteca digital del ITLA")
                exit()
            else:
                print("Respuesta Invalida. Por Favor Ingrese Si o No")
                break
    
    elif option == 4:
        print("Gracias por utilizar nuestros servicios")
        exit()

    else:
        print("Opcion invalida")
        break


