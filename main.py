from design.irregular_solids import tableIrregularSolids, designIrregularSolidThingToDo, designCalculatesOfIrregularSolids, designIrregularSolidCloud
from design.regular_solids import tableRegularSolids, designRegularSolidThingToDo, designCalculatesOfRegularSolids

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
                case 1:
                    print(
                        "Por ahora tengo estos sólidos irregulares en mi base de datos."
                    )
                    tableIrregularSolids()
                    match designIrregularSolidThingToDo():
                        case 1 : 
                            match designCalculatesOfIrregularSolids():
                                case 1 :
                                    match designIrregularSolidCloud():
                                        case 1 : print("calculo 1")
                                        case 2 : print("calculo 2")
                                        case 3 : print("calculo 1")
                                        case 4 : print("calculo 1")
                                        case 5 : print("calculo 1")
                                        case 6 : break
                                        case _:
                                            print(
                                                "La opcion ingresada no esta dentro de las opciones anteriores."
                                            )
                        case 2 : 
                            match designCalculatesOfIrregularSolids():
                                case 1 :print("Calculo 1")
                        case 3 : 
                            match designCalculatesOfIrregularSolids():
                                case 1 :print("Calculo 1")
                        case 4 : break
                        case _:
                            print(
                                "La opcion ingresada no esta dentro de las opciones anteriores."
                            )
                case 2:
                    print(
                        "Por ahora tengo estos sólidos regulares en mi base de datos."
                    )
                    tableRegularSolids()
                    match designRegularSolidThingToDo():
                        case 1 : 
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 2 :
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 3 : 
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 4 : 
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 5 :
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 6 : 
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 7 :
                            match designCalculatesOfRegularSolids():
                                case 1 : print("Calculo 1")
                        case 8 : break
                        case _:
                            print(
                                "La opcion ingresada no esta dentro de las opciones anteriores."
                            )
                case 3:
                    print("Hasta la próxima :) ")
                    break
                case _:
                    print(
                        "La opcion ingresada no esta dentro de las opciones anteriores."
                    )
    except ValueError:
        print("Por favor, ingrese un número.")