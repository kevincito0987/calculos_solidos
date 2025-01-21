import tabulate
from logic.regular_solids import findAllRegularSolids

def tableRegularSolids():
    data = findAllRegularSolids()
    # Utilizando comprensión de listas para crear una nueva lista sin la clave "calculos"
    data_modify = [{k: v for k, v in d.items() if k != "variables"} for d in data]

    print(tabulate.tabulate(data_modify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))

def designRegularSolidThingToDo():
    print(
        """
            ===========================================
                    Solido Irregular a Calcular
            ===========================================
            ¿Qué solido irregular deseas calcular?
            1. Calculos de la Cubo
            2. Calculos de la Esfera
            3. Calculos de la Cilindro
            4. Calculos de la Prisma rectangular
            5. Calculos de la Cono
            6. Calculos de la Pirámide cuadrangular regular
            7. Calculos de la Octaedro regular
            8. Regresar al Menú Principal
            ===========================================
            Selecciona una opción (1-8):
          """
    )
    opc = int(input())
    return opc

def designCalculatesOfRegularSolids():
    print(
        """
            ===========================================
               Calculos del Solido Regular a Calcular
            ===========================================
            ¿Qué solido irregular deseas calcular?
            1. Calcular Volumen
            2. Calculos Área
            3. Calculos Masa
            3. Calculos Densidad
            5. Regresar al Menú Principal
            ===========================================
            Selecciona una opción (1-8):
          """
    )
    opc = int(input())
    return opc