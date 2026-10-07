from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# Intentar conexión con timeout de 2 segundos
try:
    client = MongoClient("mongodb://127.0.0.1:27017/", serverSelectionTimeoutMS=2000)
    client.admin.command('ping')
    db = client["emprendimiento_sena_lab"]
    
    if db.asesorias_demo.count_documents({"_id": "ASE-DEMO-001"}) == 0:
        db.asesorias_demo.insert_one({
            "_id": "ASE-DEMO-001",
            "emprendedor_alias": "Emprendedor ficticio 01",
            "iniciativa": {
                "codigo": "INI-DEMO-001",
                "nombre": "EcoEmpaque",
                "sector": "economia_circular"
            },
            "temas": ["propuesta de valor", "validacion de clientes"],
            "modalidad": "virtual",
            "estado": "programada",
            "requiere_seguimiento": True,
            "fecha_programada": datetime.fromisoformat("2026-10-08T13:00:00"),
            "fecha_realizacion": None
        })
    doc = db.asesorias_demo.find_one({"_id": "ASE-DEMO-001"})
    print("--- Conectado a MongoDB local ---")
    print(doc)
    print("\nEs de tipo Date/datetime?:", isinstance(doc["fecha_programada"], datetime))

except ServerSelectionTimeoutError:
    # Si MongoDB no está corriendo, muestra el documento de laboratorio en pantalla
    print("--- Servidor MongoDB no detectado. Mostrando estructura del documento ---")
    doc = {
        "_id": "ASE-DEMO-001",
        "emprendedor_alias": "Emprendedor ficticio 01",
        "iniciativa": {
            "codigo": "INI-DEMO-001",
            "nombre": "EcoEmpaque",
            "sector": "economia_circular"
        },
        "temas": ["propuesta de valor", "validacion de clientes"],
        "modalidad": "virtual",
        "estado": "programada",
        "requiere_seguimiento": True,
        "fecha_programada": datetime.fromisoformat("2026-10-08T13:00:00"),
        "fecha_realizacion": None
    }
    print(doc)
    print("\nEs de tipo Date/datetime?:", isinstance(doc["fecha_programada"], datetime))


#Parte 1 (Lectura y corrección de JSON):
#Bash
#python p1_json.py

#Parte 2 (Filtrado de datos en Python):
#Bash
#python p2_filtrar.py

#Parte 3 (Consulta SQL en base de datos relacional):
#Bash
#python p3_sql.py

#Parte 4 (Verificación de documento y fecha en NoSQL):
#Bash
#python 01_explorar.py
