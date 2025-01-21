import json

def findAllIrregularSolids():
    try:
        with open("data/irregularSolids.json", "r") as f:
            data = f.read()
            converted = json.loads(data)
            return converted
    except json.JSONDecodeError as e:
        print("Error al leer el archivo JSON:", e)
        return []
    