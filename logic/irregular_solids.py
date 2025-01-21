import json
from math import sqrt, pi 

def findAllIrregularSolids():
    try:
        with open("data/irregularSolids.json", "r") as f:
            data = f.read()
            converted = json.loads(data)
            return converted
    except json.JSONDecodeError as e:
        print("Error al leer el archivo JSON:", e)
        return []

def calculateVolumeEllipsoidCloud():
    print("""
    Recordemos que en una nube con forma Elipsoide se deve pasar valores de paramatros para calcular su vólumen, 
          ejemplo: ("parametros":
                            "a": 1000, 
                            "b": 500,  
                            "c": 200   
                        )
    """)
    a = float(input("Ingresa el valor del primer parametro: "))
    b = float(input("Ingresa el valor del segundo parametro: "))
    c = float(input("Ingresa el valor del tercer parametro: "))
    result = (4/3) * pi * a * b * c

    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateVolumeSphereCloud():
    print("""
    Recordemos que en una nube con forma de Esfera se deve pasar valores de paramatros para calcular su vólumen, 
          ejemplo: ("parametros":
                            "r": 500
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    result =  (4/3) * pi * (r*r*r)
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateVolumeCylinderCloud():
    print("""
    Recordemos que en una nube con forma de Cilindro se deve pasar valores de paramatros para calcular su vólumen, 
          ejemplo: ("parametros":
                            "r": 200,
                            "h": 1000 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  pi * (r*r) * h
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateVolumePrismCloud():
    print("""
    Recordemos que en una nube con forma de Prisma se deve pasar valores de paramatros para calcular su vólumen, 
          ejemplo: ("parametros":
                            "Area_base": 50000,
                            "altura": 800 
                        )
    """)
    baseArea = float(input("Ingresa el valor del parametro area_base: "))
    height = float(input("Ingresa el valor del parametro altura: "))

    result =  baseArea * height
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateVolumeLenticularCloud():
    print("""
    Recordemos que en una nube con forma Lenticular se deve pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300, 
                            "h": 200 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  pi * (r*r) * h
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateMassEllipsoidCloud():
    print("""
    Recordemos que en una nube con forma Elipsoide se deve pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "a": 1000, 
                            "b": 500,  
                            "c": 200   
                        )
    """)
    a = float(input("Ingresa el valor del primer parametro: "))
    b = float(input("Ingresa el valor del segundo parametro: "))
    c = float(input("Ingresa el valor del tercer parametro: "))
    result = 0.5 * (4/3) * pi * a * b * c

    print(f"La masa total de la nube con forma de Elipsoide es de {result}")

def calculateMassSphereCloud():
    print("""
    Recordemos que en una nube con forma de Esfera se deve pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 500
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    result =  0.5 * (4/3) * pi * (r*r*r)
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateMassCylinderCloud():
    print("""
    Recordemos que en una nube con forma de Cilindro se deve pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 200,
                            "h": 1000 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  0.5 * pi * (r*r) * h
    print(f"La masa total de la nube con forma de Elipsoide es de {result}")

def calculateMassPrismCloud():
    print("""
    Recordemos que en una nube con forma de Prisma se deve pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "Area_base": 50000,
                            "altura": 800 
                        )
    """)
    baseArea = float(input("Ingresa el valor del parametro area_base: "))
    height = float(input("Ingresa el valor del parametro altura: "))

    result =  0.5 * baseArea * height
    print(f"La masa total de la nube con forma de Elipsoide es de {result}")

def calculateMassLenticularCloud():
    print("""
    Recordemos que en una nube con forma Lenticular se deve pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 300, 
                            "h": 200 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  0.5 * pi * (r*r) * h
    print(f"La masa total de la nube con forma de Elipsoide es de {result}")

def calculateDensytyEllipsoidCloud():
    print("""
    Recordemos que en una nube con forma Elipsoide se deve pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "a": 1000, 
                            "b": 500,  
                            "c": 200   
                        )
    """)
    a = float(input("Ingresa el valor del primer parametro: "))
    b = float(input("Ingresa el valor del segundo parametro: "))
    c = float(input("Ingresa el valor del tercer parametro: "))
    result = 0.5 * (4/3) * pi * a * b * c / ((4/3) * pi * a * b * c)

    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateDensitySphereCloud():
    print("""
    Recordemos que en una nube con forma de Esfera se deve pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 500
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    result =  0.5 * (4/3) * pi * (r*r*r) / (4/3) * pi * (r*r*r) 
    print(f"La densidad total de la nube con forma de Elipsoide es de {result}")

def calculateDensityCylinderCloud():
    print("""
    Recordemos que en una nube con forma de Cilindro se deve pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 200,
                            "h": 1000 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  0.5 * pi * (r*r) * h / pi * (r*r) * h
    print(f"La densidad total de la nube con forma de Elipsoide es de {result}")

def calculateDensityPrismCloud():
    print("""
    Recordemos que en una nube con forma de Prisma se deve pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "Area_base": 50000,
                            "altura": 800 
                        )
    """)
    baseArea = float(input("Ingresa el valor del parametro area_base: "))
    height = float(input("Ingresa el valor del parametro altura: "))

    result = 0.5 * baseArea * height / baseArea * height
    print(f"La densidad total de la nube con forma de Elipsoide es de {result}")

def calculateDensityLenticularCloud():
    print("""
    Recordemos que en una nube con forma Lenticular se deve pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300, 
                            "h": 200 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  0.5 * pi * (r*r) * h / pi * (r*r) * h
    print(f"La densidad total de la nube con forma de Elipsoide es de {result}")