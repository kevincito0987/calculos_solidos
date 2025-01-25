import json
from math import pi

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
    Recordemos que en una nube con forma Elipsoide se debe pasar valores de paramatros para calcular su vólumen, 
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
    Recordemos que en una nube con forma de Esfera se debe pasar valores de paramatros para calcular su vólumen, 
          ejemplo: ("parametros":
                            "r": 500
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    result =  (4/3) * pi * (r*r*r)
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateVolumeCylinderCloud():
    print("""
    Recordemos que en una nube con forma de Cilindro se debe pasar valores de paramatros para calcular su vólumen, 
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
    Recordemos que en una nube con forma de Prisma se debe pasar valores de paramatros para calcular su vólumen, 
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
    Recordemos que en una nube con forma Lenticular se debe pasar valores de paramatros para calcular su masa, 
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
    Recordemos que en una nube con forma Elipsoide se debe pasar valores de paramatros para calcular su masa, 
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
    Recordemos que en una nube con forma de Esfera se debe pasar valores de paramatros para calcular su masa, 
          ejemplo: ("parametros":
                            "r": 500
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    result =  0.5 * (4/3) * pi * (r*r*r)
    print(f"El volumen total de la nube con forma de Elipsoide es de {result}")

def calculateMassCylinderCloud():
    print("""
    Recordemos que en una nube con forma de Cilindro se debe pasar valores de paramatros para calcular su masa, 
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
    Recordemos que en una nube con forma de Prisma se debe pasar valores de paramatros para calcular su masa, 
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
    Recordemos que en una nube con forma Lenticular se debe pasar valores de paramatros para calcular su masa, 
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
    Recordemos que en una nube con forma Elipsoide se debe pasar valores de paramatros para calcular su densidad, 
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
    Recordemos que en una nube con forma de Esfera se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 500
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    result =  0.5 * (4/3) * pi * (r*r*r) / (4/3) * pi * (r*r*r) 
    print(f"La densidad total de la nube con forma de Elipsoide es de {result}")

def calculateDensityCylinderCloud():
    print("""
    Recordemos que en una nube con forma de Cilindro se debe pasar valores de paramatros para calcular su densidad, 
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
    Recordemos que en una nube con forma de Prisma se debe pasar valores de paramatros para calcular su densidad, 
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
    Recordemos que en una nube con forma Lenticular se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300, 
                            "h": 200 
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  0.5 * pi * (r*r) * h / pi * (r*r) * h
    print(f"La densidad total de la nube con forma de Elipsoide es de {result}")

def calculateVolumeOfMountain():
    print("""
    Recordemos que en una montaña se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (radio), 
                            "h": 200 (altura)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  (1/3) * pi * (r*r) * h
    print(f"El volumen total de la montaña es de {result}")


def calculateAreaOfMountain():
    print("""
    Recordemos que en una montaña se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (radio), 
                            "h": 200 (altura)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =  r * h
    print(f"El area total de la montaña es de {result}")


def calculateDensityOfMountain():
    print("""
    Recordemos que en una montaña se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (radio), 
                            "h": 200 (altura),
                            "m": 300 (masa)
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))
    m = float(input("Ingresa el valor del parametro m: "))

    result = m / (1/3) * pi* (r*r) * h
    print(f"La densidad total de la montaña es de {result}")

def calculateVolumeOfSeaStar():
    print("""
    Recordemos que en una estrella de mar se debe pasar valores de paramatros para calcular su area, 
          ejemplo: ("parametros":
                            "r": 300 (radio de las esferas de la estrella de mar.), 
                            "h": 200 (numero de esferas),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = 4 * pi * h * (r*r)
    print(f"El area total de la estrella de mar es de {result}")

def calculateAreaOfSeaStar():
    print("""
    Recordemos que en una estrella de mar se debe pasar valores de paramatros para calcular su volumen, 
          ejemplo: ("parametros":
                            "r": 300 (radio de las esferas de la estrella de mar.), 
                            "h": 200 (numero de esferas),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result = pi * (1/3) * h * (r*r*r)
    print(f"El volumen total de la estrella de mar es de {result}")

def calculateDensityOfSeaStar():
    print("""
    Recordemos que en una estrella de mar se debe pasar valores de paramatros para calcular su densidad, 
          ejemplo: ("parametros":
                            "r": 300 (masa de la estrella de mar.), 
                            "h": 200 (volumen de la estrella de mar),
                        )
    """)
    r = float(input("Ingresa el valor del parametro r: "))
    h = float(input("Ingresa el valor del parametro h: "))

    result =r / h
    print(f"La densidad total de la estrella de mar es de {result}")