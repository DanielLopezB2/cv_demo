import os
from PIL import Image

# Define la ruta a la carpeta que contiene las imágenes
carpeta = 'Image-Treatment/BarbellSquat'

# Carpeta donde se guardaran las imagenes
carpeta_objetivo = 'Image-Treatment/BarbellSquat'

# Define el tamaño objetivo para las imágenes
tamaño_objetivo = (500, 500)

# Lista todos los archivos en la carpeta
archivos = os.listdir(carpeta)

# Recorre todos los archivos en la carpeta
for archivo in archivos:
    # Comprueba si el archivo es una imagen JPG
    if archivo.endswith('.jpg'):
        # Abre la imagen en formato JPG
        img = Image.open(os.path.join(carpeta, archivo))

        # Redimensiona la imagen al tamaño objetivo
        img_redimensionada = img.resize(tamaño_objetivo)
        
        # Divide el nombre del archivo en el nombre base y la extensión
        nombre_base, _ = os.path.splitext(archivo)
        
        # Crea el nombre del archivo de salida con el tamaño objetivo
        archivo_salida = f"{nombre_base}{tamaño_objetivo[0]}x{tamaño_objetivo[1]}.jpg"

        # Guarda la imagen redimensionada
        img_redimensionada.save(os.path.join(carpeta_objetivo, archivo))
