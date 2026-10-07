# Lista de iniciativas brindada por la guía
iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"} # Ojo: Campo 'pendiente' ausente
]

def seleccionar_pendientes(registros, sector):
    codigos_pendientes = []
    
    for item in registros:
        # 1. Comprobar que coincida el sector
        # 2. Usar item.get('pendiente') para evitar que falle si el campo está ausente.
        # 3. Usar 'is True' para asegurar que sea exactamente el booleano True y no una cadena "True".
        if item.get("sector") == sector and item.get("pendiente") is True:
            codigos_pendientes.append(item["codigo"])
            
    return codigos_pendientes

# Pruebas exigidas
print("--- Prueba 1: Sector 'tecnologia' (debe retornar ['INI-001']) ---")
resultado_tec = seleccionar_pendientes(iniciativas, "tecnologia")
print("Resultado:", resultado_tec)

print("\n--- Prueba 2: Sector 'economia_circular' (sin resultados, retorna []) ---")
resultado_vacio = seleccionar_pendientes(iniciativas, "economia_circular")
print("Resultado:", resultado_vacio)