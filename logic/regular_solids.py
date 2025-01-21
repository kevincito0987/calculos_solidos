import json

def findAllRegularSolids():
    try:
        with open("data/regularSolids.json", "r") as f:
            data = f.read()
            converted = json.loads(data)
            return converted
    except json.JSONDecodeError as e:
        print("Error al leer el archivo JSON:", e)
        return []
    