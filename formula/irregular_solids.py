import tabulate
from logic.regular_solids import findAllRegularSolids

def tableIrregularSolids():
    data = findAllRegularSolids()
    # Utilizando comprensión de listas para crear una nueva lista sin la clave "calculos"
    data_modify = [{k: v for k, v in d.items() if k != "calculos"} for d in data]

    print(tabulate.tabulate(data_modify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))