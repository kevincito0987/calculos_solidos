from design.irregular_solids import tableIrregularSolids, designIrregularSolidThingToDo, designCalculatesOfIrregularSolids, designIrregularSolidCloud, designCalculatesOfIrregularSolidsMountainAndSeaStar
from design.regular_solids import tableRegularSolids, designRegularSolidThingToDo, designCalculatesOfRegularSolids
from logic.irregular_solids import calculateVolumeEllipsoidCloud, calculateVolumeSphereCloud, calculateVolumeCylinderCloud, calculateVolumePrismCloud, calculateVolumeLenticularCloud, calculateMassEllipsoidCloud, calculateMassSphereCloud, calculateMassCylinderCloud, calculateMassPrismCloud, calculateMassLenticularCloud, calculateDensytyEllipsoidCloud, calculateDensitySphereCloud, calculateDensityCylinderCloud, calculateDensityPrismCloud, calculateDensityLenticularCloud, calculateAreaOfMountain, calculateDensityOfMountain, calculateVolumeOfMountain, calculateDensityOfSeaStar, calculateAreaOfSeaStar, calculateVolumeOfSeaStar
from logic.regular_solids import calculateVolumeCube, calculateMassCube, calculateAreaCube, calculateDensityCube, calculatDensitySphere, calculateAreaSphere, calculateMassSphere, calculateVolumeSphere, calculateAreaCylinder, calculateDensityCylinder, calculateMassCylinder, calculateVolumeCylinder, calculateAreaRectangularPrism, calculateDensityRectangularPrism, calculateMassRectangularPrism, calculateVolumeRectangularPrism, calculateAreaCone, calculateDensityCone, calculateMassCone, calculateVolumeCone, calculateAreaRegularQuadrangularPyramid, calculateDensityRegularQuadrangularPyramid, calculateMassRegularQuadrangularPyramid, calculateVolumeRegularQuadrangularPyramid, calculateAreaRegularOctahedron, calculateDensityRegularOctahedron,calculateMassRegularOctahedron, calculateVolumeRegularOctahedron

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
                                match designCalculatesOfIrregularSolidsMountainAndSeaStar():
                                    case 1 : calculateVolumeOfSeaStar()
                                    case 2 : calculateAreaOfSeaStar()
                                    case 3 : calculateDensityOfSeaStar()
                                    case 4 : break
                                    case _:
                                            print(
                                                        "La opcion ingresada no esta dentro de las opciones anteriores."
                                                    )
                            case 3 : 
                                match designCalculatesOfIrregularSolidsMountainAndSeaStar():
                                    case 1 : calculateVolumeOfMountain()
                                    case 2 : calculateAreaOfMountain()
                                    case 3 : calculateDensityOfMountain()
                                    case 4 : break
                                    case _:
                                            print(
                                                        "La opcion ingresada no esta dentro de las opciones anteriores."
                                                    )
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
                                    case 1 : calculateVolumeCube()
                                    case 2 : calculateAreaCube()
                                    case 3 : calculateMassCube()
                                    case 4 : calculateDensityCube()
                                    case 4 : break
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
                            case 2 :
                                match designCalculatesOfRegularSolids():
                                    case 1 : calculateVolumeSphere()
                                    case 2 : calculateAreaSphere()
                                    case 3 : calculateMassSphere()
                                    case 4 : calculatDensitySphere()
                                    case 4 : break
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
                            case 3 : 
                                match designCalculatesOfRegularSolids():
                                    case 1 : calculateVolumeCylinder()
                                    case 2 : calculateAreaCylinder()
                                    case 3 : calculateMassCylinder()
                                    case 4 : calculateDensityCylinder()
                                    case 4 : break
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
                            case 4 : 
                                match designCalculatesOfRegularSolids():
                                    case 1 : calculateVolumeRectangularPrism()
                                    case 2 : calculateAreaRectangularPrism()
                                    case 3 : calculateMassRectangularPrism()
                                    case 4 : calculateDensityRectangularPrism()
                                    case 4 : break
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
                            case 5 :
                                match designCalculatesOfRegularSolids():
                                    case 1 : calculateVolumeCone()
                                    case 2 : calculateAreaCone()
                                    case 3 : calculateMassCone()
                                    case 4 : calculateDensityCube()
                                    case 4 : break
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
                            case 6 : 
                                match designCalculatesOfRegularSolids():
                                    case 1 : calculateVolumeRegularQuadrangularPyramid()
                                    case 2 : calculateAreaRegularQuadrangularPyramid()
                                    case 3 : calculateMassRegularQuadrangularPyramid()
                                    case 4 : calculateDensityRegularQuadrangularPyramid()
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
                            case 7 :
                                match designCalculatesOfRegularSolids():
                                    case 1 : calculateVolumeRegularOctahedron()
                                    case 2 : calculateAreaRegularOctahedron()
                                    case 3 : calculateMassRegularOctahedron()
                                    case 4 : calculateDensityRegularOctahedron()
                                    case 4 : calculateDensityRegularQuadrangularPyramid()
                                    case _:
                                        print(
                                            "La opcion ingresada no esta dentro de las opciones anteriores."
                                        )
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