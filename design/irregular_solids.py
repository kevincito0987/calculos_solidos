import tabulate
from logic.irregular_solids import findAllIrregularSolids

def tableIrregularSolids():
    data = findAllIrregularSolids()
    # Utilizando comprensión de listas para crear una nueva lista sin la clave "calculos"
    data_modify = [{k: v for k, v in d.items() if k != "calculos"} for d in data]

    print(tabulate.tabulate(data_modify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))


def designIrregularSolidThingToDo():
    print(
        """
            ===========================================
                    Solido Irregular a Calcular
            ===========================================
            ¿Qué solido irregular deseas calcular?
            1. Calculos de la Nube
            2. Calculos de la Esponja de mar
            3. Calculos de la Montaña
            4. Regresar al Menú Principal
            ===========================================
            Selecciona una opción (1-4):
          """
    )
    opc = int(input())
    return opc

def designCalculatesOfIrregularSolids():
    print(
        """
            ==============================================
               Calculos del Solido Irregular a Calcular
            ==============================================
            ¿Qué solido irregular deseas calcular?
            1. Calcular Volumen
            2. Calculos Masa
            3. Calculos Densidad
            4. Regresar al Menú Principal
            ===========================================
            Selecciona una opción (1-4):
          """
    )
    opc = int(input())
    return opc

def designIrregularSolidCloud():
    print(
        """
            ===========================================
                    Forma de la Nube a Calcular
            ===========================================
            ¿Qué forma vas a calcular?
            1. Elipsoide
            2. Esfera
            3. Cilindro
            4. Esfera
            5. Cilindro
            6. Regresar al Menú Principal
            ===========================================
            Selecciona una opción (1-6):
          """
    )
    opc = int(input())
    return opc

def designCalculatesOfIrregularSolidsMountainAndSeaStar():
    print(
        """
            ==============================================
               Calculos del Solido Irregular a Calcular
            ==============================================
            ¿Qué solido irregular deseas calcular?
            1. Calcular Volumen
            2. Calculos area
            3. Calculos Densidad
            4. Regresar al Menú Principal
            ===========================================
            Selecciona una opción (1-4):
          """
    )
    opc = int(input())
    return opc
