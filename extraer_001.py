import subprocess
import os

carpeta = "correos"

for archivo in os.listdir(carpeta):
    if archivo.endswith(".txt"):

        ruta = os.path.join(carpeta, archivo)

        with open(ruta, "r", encoding="utf-8") as f:
            correo = f.read()

        prompt = f"""
Extrae:

Nombre completo
Empresa
Puesto

Responde solo en formato:

Nombre:
Empresa:
Puesto:

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

        print(f"\n--- Resultado para {archivo} ---")
        print(resultado.stdout)
