from design.irregular_solids import tableIrregularSolids, designIrregularSolidThingToDo, designCalculatesOfIrregularSolids, designIrregularSolidCloud
from design.regular_solids import tableRegularSolids, designRegularSolidThingToDo, designCalculatesOfRegularSolids
from logic.irregular_solids import calculateVolumeEllipsoidCloud, calculateVolumeSphereCloud, calculateVolumeCylinderCloud, calculateVolumePrismCloud, calculateVolumeLenticularCloud, calculateMassEllipsoidCloud, calculateMassSphereCloud, calculateMassCylinderCloud, calculateMassPrismCloud, calculateMassLenticularCloud, calculateDensytyEllipsoidCloud, calculateDensitySphereCloud, calculateDensityCylinderCloud, calculateDensityPrismCloud, calculateDensityLenticularCloud

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
                    while True: 
                        print(
                            "Por ahora tengo estos sólidos irregulares en mi base de datos."
                        )
                        tableIrregularSolids()
                        match designIrregularSolidThingToDo():
                            case 1 : 
                                match designCalculatesOfIrregularSolids():
                                    case 1 :
                                        match designIrregularSolidCloud():
                                            case 1 : calculateVolumeEllipsoidCloud()
                                            case 2 : calculateVolumeSphereCloud()
                                            case 3 : calculateVolumeCylinderCloud()
                                            case 4 : calculateVolumePrismCloud()
                                            case 5 : calculateVolumeLenticularCloud()
                                            case 6 : break
                                            case _:
                                                print(
                                                    "La opcion ingresada no esta dentro de las opciones anteriores."
                                                )
                                    case 2 : 
                                          match designIrregularSolidCloud():
                                               case 1 : calculateMassEllipsoidCloud()
                                               case 2 : calculateMassSphereCloud()
                                               case 3 : calculateMassCylinderCloud()
                                               case 4: calculateMassPrismCloud()
                                               case 5 : calculateMassLenticularCloud()
                                               case 6 : break
                                               case _:
                                                    print(
                                                        "La opcion ingresada no esta dentro de las opciones anteriores."
                                                    )
                                    case 3 :
                                          match designIrregularSolidCloud(): 
                                               case 1 : calculateDensytyEllipsoidCloud()
                                               case 2 : calculateDensitySphereCloud()
                                               case 3 : calculateDensityCylinderCloud()
                                               case 4 : calculateDensityPrismCloud()
                                               case 5 : calculateDensityLenticularCloud()
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
                        volver = input(
                                    "¿Deseas continuar en el menu de Calcular Sólidos Irregulares.? (s/n): "
                                )
                        if volver.lower() == "s":
                                    continue  # Se queda en el menú de productos
                        else:
                                    break
                case 2:
                    while True:
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
                        volver = input(
                                    "¿Deseas continuar en el menu de Calcular Sólidos Regulares? (s/n): "
                                )
                        if volver.lower() == "s":
                                    continue  # Se queda en el menú de productos
                        else:
                                    break
                case 3:
                    print("Hasta la próxima :) ")
                    break
                case _:
                    print(
                        "La opcion ingresada no esta dentro de las opciones anteriores."
                    )
    except ValueError:
        print("Por favor, ingrese un número.")