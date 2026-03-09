import subprocess
import sys

# recibir texto desde leer_correos.py
correo = sys.stdin.read()

prompt = f"""
Extrae EXACTAMENTE la información del texto.

Reglas:
- Nombre completo completo (no solo el primer nombre)
- Empresa o razón social completa
- Puesto o profesión

Responde SOLO en este formato:
Nombre Completo|Empresa|Puesto

Texto:
{correo}
"""

resultado = subprocess.run(
    ["ollama", "run", "phi3"],
    input=prompt,
    text=True,
    capture_output=True,
    encoding="utf-8"
)

print(resultado.stdout.strip())
