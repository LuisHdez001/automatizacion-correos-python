import os

carpeta = "correos/basico"

for archivo in os.listdir(carpeta):
    print("Procesando:", archivo)
