import random

while True:
    print("""En que numero estoy pensando? intenta adivinar.
      1. Quieres Jugar?
      2. Salir""")

    option = int(input("Itroduce una opcion: "))
    if option == 1:
        adivina = random.randint(1, 50)
        while True: 
            numero = int(input("En que numero estoy pensando. un numero del 1 al 50?: "))
            if numero > adivina:
                print("numero muy alto intenta un numero menos")
            
            elif numero < adivina:
                print("numero muy bajo intenta un numero mas alto")
          
            elif numero == adivina:
                print("Felicidades, adivinaste el numero en que estaba pensando, que es: ", adivina)
            volver = str(input("Quieres volver a jugar? (s/n): "))
            if volver.lower() != "s":
                break
    elif option == 2:
        print("Saliendo del programa. Gracias por jugar.")
        exit()
        
    else:
        print("opcion invalida")
            