import json
from math import pi, sqrt

def findAllRegularSolids():
    try:
        with open("data/regularSolids.json", "r") as f:
            data = f.read()
            converted = json.loads(data)
            return converted
    except json.JSONDecodeError as e:
        print("Error al leer el archivo JSON:", e)
        return []
    
def calculateVolumeCube():
    print("""
    Recordemos que en un cubo se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (valor de un lado del cubo.), 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))

    result = (r*r*r)
    print(f"El volumen total del cubo es de {result}")

def calculateAreaCube():
    print("""
    Recordemos que en un cubo se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (valor de un lado del cubo.), 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))

    result = 6 * (r*r)
    print(f"El area total del cubo es de {result}")

def calculateMassCube():
    print("""
    Recordemos que en un cubo se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (valor de un lado del cubo.), 
                            "h": 300 (valor de la densidad del cubo.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = h * (r*r*r)
    print(f"La masa total del cubo es de {result}")

def calculateDensityCube():
    print("""
    Recordemos que en un cubo se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (valor de un lado del cubo.), 
                            "h": 300 (valor de la masa del cubo.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = h / (r*r*r)
    print(f"La densidad total del cubo es de {result}")

def calculateVolumeSphere():
    print("""
    Recordemos que en una esfera se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.), 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))

    result = (4/3) * pi * (r*r*r)
    print(f"El volumen total de la esfera es de {result}")

def calculateAreaSphere():
    print("""
    Recordemos que en una esfera se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.), 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))

    result = 4 * pi * (r*r)
    print(f"El area total de la esfera es de {result}")

def calculateMassSphere():
    print("""
    Recordemos que en una esfera se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.),
                            "h": 300 (valor de la densidad.) 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = h * (4/3) * pi * (r*r*r)
    print(f"La masa total de la esfera es de {result}")

def calculatDensitySphere():
    print("""
    Recordemos que en una esfera se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.),
                            "h": 300 (valor de la masa del cubo.) 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = h / ((4/3) * pi * (r*r*r))
    print(f"La densidad total de la esfera es de {result}")

def calculateVolumeCylinder():
    print("""
    Recordemos que en un cilindro se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.),
                            "h": 300 (valor de la altura.) 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = pi * (r*r) * h
    print(f"El volumen total del cilindro es de {result}")

def calculateAreaCylinder():
    print("""
    Recordemos que en un cilindro se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.),
                            "h": 300 (valor de la altura.) 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = 2 * pi * r * (r+h)
    print(f"El area total del cilindro es de {result}")

def calculateMassCylinder():
    print("""
    Recordemos que en un cilindro se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.),
                            "h": 300 (valor de la altura.)
                            "d": 300 (valor de la densidad.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result = d * pi * (r*r) * h
    print(f"La masa total del cilindro es de {result}")

def calculateDensityCylinder():
    print("""
    Recordemos que en un cilindro se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (radio de la esfera.),
                            "h": 300 (valor de la altura.)
                            "d": 300 (valor de la masa.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result = d / (pi * (r*r) * h)
    print(f"La densidad total del cilindro es de {result}")

def calculateVolumeRectangularPrism():
    print("""
    Recordemos que en un prisma rectangular se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (largo.),
                            "h": 300 (alto.)
                            "d": 300 (ancho.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result = r * h * d
    print(f"El volumen total del prisma rectangular es de {result}")

def calculateAreaRectangularPrism():
    print("""
    Recordemos que en un prisma rectangular se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (largo.),
                            "h": 300 (alto.)
                            "d": 300 (ancho.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result = 2 * ((r*d) + (r*h) + (d*h))
    print(f"El area total del prisma rectangular es de {result}")

def calculateMassRectangularPrism():
    print("""
    Recordemos que en un prisma rectangular se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (largo.),
                            "h": 300 (alto.)
                            "a": 300 (ancho.)
                            "d": 300 (densidad.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))
    a = float(input("Ingresa el valor del parametro d: "))

    result =  d * r * a * h
    print(f"La masa total del prisma rectangular es de {result}")

def calculateDensityRectangularPrism():
    print("""
    Recordemos que en un prisma rectangular se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (largo.),
                            "h": 300 (alto.)
                            "a": 300 (ancho.)
                            "d": 300 (masa.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))
    a = float(input("Ingresa el valor del parametro d: "))

    result =  d / (r * h * a)
    print(f"La masa total del prisma rectangular es de {result}")

def calculateVolumeCone():
    print("""
    Recordemos que en un cono se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (radio.),
                            "h": 300 (altura.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  (1/3) * pi * (r*r) * h
    print(f"El volumen total del cono es de {result}")

def calculateAreaCone():
    print("""
    Recordemos que en un cono se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (radio.),
                            "h": 300 (altura.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  pi * r * (r + sqrt((h*h) + (r*r)))
    print(f"El area total del cono es de {result}")

def calculateMassCone():
    print("""
    Recordemos que en un cono se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (radio.),
                            "h": 300 (altura.)
                            "d": 300 (densida.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result =  d * (1/3) * pi * (r*r) * h
    print(f"La masa total del cono es de {result}")

def calculateDensityCone():
    print("""
    Recordemos que en un cono se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (radio.),
                            "h": 300 (altura.)
                            "d": 300 (densida.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result =  d / ((1/3) * pi * (r*r) * h)
    print(f"La densidad total del cono es de {result}")

def calculateVolumeRegularQuadrangularPyramid():
    print("""
    Recordemos que en una Pirámide cuadrangular regular se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                            "h": 300 (altura.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  (1/3) * (r*r) * h
    print(f"El volumen total de la Pirámide cuadrangular regular es de {result}")

def calculateAreaRegularQuadrangularPyramid():
    print("""
    Recordemos que en una Pirámide cuadrangular regular se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                            "h": 300 (altura.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  (r*r) + 2 * r * sqrt((h*h) + ((r/2)*(r/2)))
    print(f"El area total de la Pirámide cuadrangular regular es de {result}")

def calculateMassRegularQuadrangularPyramid():
    print("""
    Recordemos que en una Pirámide cuadrangular regular se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                            "h": 300 (altura.)
                            "d": 300 (densidad.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result =  d * (1/3) * (r*r) * h
    print(f"La masa total de la Pirámide cuadrangular regular es de {result}")

def calculateDensityRegularQuadrangularPyramid():
    print("""
    Recordemos que en una Pirámide cuadrangular regular se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                            "h": 300 (altura.)
                            "d": 300 (masa.)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result =  d / ((1/3) * (r*r) * h)
    print(f"La densidad total de la Pirámide cuadrangular regular es de {result}")

def calculateVolumeRegularOctahedron():
    print("""
    Recordemos que en un Octaedro regular se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))

    result =  (1/3) * 2 * sqrt(2) * (r*r*r)
    print(f"El volumen total del Octaedro regular es de {result}")

def calculateAreaRegularOctahedron():
    print("""
    Recordemos que en un Octaedro regular se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))

    result =  2 * sqrt(3) * (r*r)
    print(f"El area total del Octaedro regular es de {result}")

def calculateMassRegularOctahedron():
    print("""
    Recordemos que en un Octaedro regular se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                            "d": 300 (densidad.),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result =  d / ((1/3) * 2 * sqrt(2) * (r*r*r))
    print(f"La masa total del Octaedro regular es de {result}")

def calculateDensityRegularOctahedron():
    print("""
    Recordemos que en un Octaedro regular se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (lado.),
                            "d": 300 (masa.),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    d = float(input("Ingresa el valor del parametro d: "))

    result =  d / ((1/3) * 2 * sqrt(2) * (r*r*r))
    print(f"La densidad total del Octaedro regular es de {result}")