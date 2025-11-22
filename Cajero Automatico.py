Max = 3
intentos = 0
saldo = 0
logueado = False

print("Hola Saulo, Bienvnido a tu Cajero automatico digital.")

while True: 
    if not logueado:
        pin = input("Introduce tu PIN: ")

        if pin == "0924":
            logueado = True
            print("Acceso Concedido")
    
        else:
            intentos += 1
            print("Pin Incorrecto")

            if intentos >= Max:
                print("Has alcanzado el maximo de intentos")
                break

    if logueado:
        print("""Hola Saulo Cuevas, ¿Qué quieres hacer?
            1. Consultar saldo
            2. Depositar dinero
            3. Retirar dinero
            4. Salir""")

        option = input("Elige una opcion: ")
        
        if option == '1':
                print("Tu saldo es: ", saldo)

        elif option == '2':
            deposito = float(input("Cuanto dinero quieres depositar?: "))
            if deposito >= 1000000000:
                 print("Lo siento no puedes depositar esa cantidad. intente con otra cantidad")
            elif deposito <= 1000000000:
                 saldo += deposito
            print("Dinero depositado con exito. Tu saldo actual es de: ", saldo)
        
        elif option == '3':
             retiro = float(input("¿Cuanto dinero quieres retirar?: "))
             if retiro > saldo:
                  print("Lo sentimos. No tienes saldo suficiente para retirar esa cantidad. intenta con otra")
             elif retiro <= saldo:
                saldo = saldo-retiro
                print("Retiro exitoso. saldo restante: ", saldo)

        elif option == '4':
             print("Gracias por usar nuestros servicios")
             print("\n" * 100) 
             break
        
             
            





    

    