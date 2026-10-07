import sqlite3

# Crear base de datos en memoria y llenar tablas según la guía
conexion = sqlite3.connect(":memory:")
conexion.executescript("""
CREATE TABLE emprendedores(id INTEGER PRIMARY KEY, alias TEXT);
CREATE TABLE iniciativas(
    id INTEGER PRIMARY KEY, emprendedor_id INTEGER, estado TEXT
);
INSERT INTO emprendedores VALUES(1, 'Emprendedor A'), (2, 'Emprendedor B'), (3, 'Emprendedor C');
INSERT INTO iniciativas VALUES(101, 1, 'activa'), (102, 2, 'archivada'), (103, 1, 'activa');
""")

# Consulta SQL solicitada
consulta = """
SELECT i.id AS iniciativa_id, e.alias AS emprendedor_alias
FROM iniciativas i
INNER JOIN emprendedores e ON i.emprendedor_id = e.id
WHERE i.estado = 'activa'
ORDER BY i.id ASC;
"""

if consulta:
    resultados = conexion.execute(consulta).fetchall()
    print("--- Resultado de la consulta SQL ---")
    for fila in resultados:
        print(f"Iniciativa ID: {fila[0]} | Emprendedor: {fila[1]}")

conexion.close()