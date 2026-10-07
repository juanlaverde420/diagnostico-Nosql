from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# Intentar conexión a MongoDB Atlas
try:
    client = MongoClient("mongodb+srv://juanjoselaverde20:julio2016juan2007@cluster0.a0exklj.mongodb.net/?appName=Cluster0", serverSelectionTimeoutMS=5000)
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
    print("--- Conectado a MongoDB Atlas (Nube) ---")
    print(doc)
    print("\nEs de tipo Date/datetime?:", isinstance(doc["fecha_programada"], datetime))

except ServerSelectionTimeoutError:
    # Si la conexión falla, muestra el documento de laboratorio en pantalla
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