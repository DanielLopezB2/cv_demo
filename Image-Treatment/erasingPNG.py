import os

# Define la ruta a la carpeta que contiene las imágenes
carpeta = 'CustomDataset/Images'

# Lista todos los archivos en la carpeta
archivos = os.listdir(carpeta)

# Recorre todos los archivos en la carpeta
for archivo in archivos:
    # Comprueba si el archivo es una imagen PNG
    if archivo.endswith('.png'):
        # Crea la ruta completa al archivo
        ruta_completa = os.path.join(carpeta, archivo)

        # Elimina el archivo
        os.remove(ruta_completa)
