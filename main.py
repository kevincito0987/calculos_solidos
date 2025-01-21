while True:
    try:
        while True:
            print(
                """
                        ===========================================
                            Administrador de Cálculos de Sólidos
                        ===========================================
                        1. Calcular Sólidos Irregulares.
                        2. Calcular Sólidos Regulares.
                        3.Salir
                        ===========================================
                        Selecciona una opción (1-3):
                """
            )
            opc = int(input())
            match opc:
                case 1 : print("caso 1")
                case 2: print("caso 2")
                case 3:
                    print("Hasta la próxima :) ")
                    break
                case _:
                    print(
                        "La opcion ingresada no esta dentro de las opciones anteriores."
                    )
    except ValueError:
        print("Por favor, ingrese un número.")