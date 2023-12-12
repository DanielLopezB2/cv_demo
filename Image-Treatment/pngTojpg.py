import os
from PIL import Image

# Define la ruta a la carpeta que contiene las imágenes
carpeta = 'CustomDataset/Images'

# Lista todos los archivos en la carpeta
archivos = os.listdir(carpeta)

# Recorre todos los archivos en la carpeta
for archivo in archivos:
    # Comprueba si el archivo es una imagen PNG
    if archivo.endswith('.png'):
        # Abre la imagen en formato PNG
        img_png = Image.open(os.path.join(carpeta, archivo))
        
        # Convierte la imagen a modo RGB
        img_rgb = img_png.convert('RGB')

        # Divide el nombre del archivo en el nombre base y la extensión
        nombre_base, _ = os.path.splitext(archivo)

        # Crea el nombre del archivo de salida
        archivo_salida = nombre_base + '.jpg'

        # Guarda la imagen en formato JPG
        img_rgb.save(os.path.join(carpeta, archivo_salida))
