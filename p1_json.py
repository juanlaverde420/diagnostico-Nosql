import json

# 1. Intento con la cadena original que contiene errores
texto_original = '{"codigo":"INI-001", "activa":True, "intereses":["Validar mercado",]}'

print("--- Intentando cargar JSON original ---")
try:
    datos_error = json.loads(texto_original)
except json.JSONDecodeError as e:
    print(f"Error detectado exitosamente: {e}\n")

# 2. Corregimos la sintaxis: 'true' en minúscula y eliminamos la coma sobrante
texto_corregido = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

# 3. Cargar la cadena corregida
datos = json.loads(texto_corregido)

codigo = datos["codigo"]
activa = datos["activa"]

# 4. Mostrar valores y tipos
print("--- Resultado del JSON corregido ---")
print("Codigo:", codigo, "| Tipo:", type(codigo).__name__)
print("Activa:", activa, "| Tipo:", type(activa).__name__)