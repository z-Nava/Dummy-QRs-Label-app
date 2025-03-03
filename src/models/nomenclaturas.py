# Diccionario de herramientas con sus jobs asociados
herramientas_data = {
    "BACKPACK / BRIEFCASE": {
        
    },
   "LSM": {
       
    },
    "POWER TROWEL":{

    },
    "THREADER":{

    },
    "PLATE COMPACTOR":{

    },
    "HIGH CICLE":{

    }, 
    "SUB PUMP":{

    },
    "RAMER":{

    },
    "SITE LIGHT":{

    },
    "SCREED":{

    },
    "EARLY ENTRY SAW":{

    },
}

def obtener_modelos():
    """Devuelve una lista de modelos de herramientas disponibles"""
    return list(herramientas_data.keys())

def obtener_jobs_por_modelo(modelo):
    """Devuelve los Job IDs disponibles para un modelo específico"""
    return list(herramientas_data.get(modelo, {}).keys())
