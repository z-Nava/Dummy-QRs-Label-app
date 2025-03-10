    # Diccionario de herramientas
herramientas_data = {
    "SITE LIGHT":{
            "modelo": ["SL"], # Modelo fijo
            "corrida": ["MP"], # Corrida fija
            "version": ["UL", "GB", "ANZ"], # Versiones disponibles
            "años": list(range(2020, 2031)), # Años disponibles
            "semanas": list(range(1, 53)), # Semanas del año
            "consecutivo":  list(range(1, 100)) # Consecutivo (001-099)
        
        },
    "SCREED":{
        "modelo":["CS"],
        "corrida":["MP"],
        "version":["UL"],
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 1000000))

    },
    "EARLY ENTRY SAW":{
        "modelo":["EES"],
        "corrida":["1", "2"], #GALLINA 1 #DISCO 2
        "version":["UL", "AN"],
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 100))
    },
    "BACKPACK / BRIEFCASE":{
        "modelo": ["BP", "BF"],  # Backpack (BP) o Briefcase (BF)
        "corrida": ["MP"],  # Corrida fija
        "version": ["UL"],  # Versión fija
        "años": list(range(2020, 2031)),  # Años disponibles
        "semanas": list(range(1, 53)),  # Semanas del año
        "consecutivo": list(range(1, 100))  # Consecutivo (001-099)
    },
    "LSM": {
        "modelo": ["LSM"],
        "corrida": ["TR"],
        "version": ["0", "1"], #500 = 0 501 = 1
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 1000)) #Consecutivo (001-999)
    },
    "POWER TROWEL":{
        "modelo":["PT24", "PT36"],
        "version":["UL", "EMEA"],
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 1000))
    },
    "THREADER":{
        "modelo":["TH"],
        "corrida":["MP"],
        "version":["UL", "EMEA", "ANZ"],
        "tipo":["1", "2"], #FUNCIONAL 1 BOMBA 2
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 10000))

    },
    "PLATE COMPACTOR":{
        "modelo":["PC"],
        "tipo":["1", "2", "3", "4"], #EXCITER 1, EXCITER 2, ELECTRONIC HOUSING 3, HANDLE BAR 4
        "version":["UL", "EMEA", "ANZ", "JP"],
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 1000))

    },
    "HIGH CICLE": {
       
    },

    "SUB PUMP":{
        "modelo":["SP"],
        "corrida":["TR", "QB", "CR", "MP"],
        "tipo":["G1", "G2"], #G1 = POWER UNIT G2 = BOMBA
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 100))

    },
    "RAMER":{
        "modelo":["R"],
        "tipo":["1", "2", "3"], #1 = CRANKCASE 2 = GALLINA 3 = HANDLEBAR
        "version":["UL", "EMEA", "ANZ"],
        "corrida":["TR", "QB", "CR", "MP"],
        "años": list(range(2020, 2031)),
        "semanas": list(range(1, 53)),
        "consecutivo": list(range(1, 1000))

    },   
}

def obtener_modelos():
    """Devuelve una lista de modelos de herramientas disponibles"""
    return list(herramientas_data.keys())

