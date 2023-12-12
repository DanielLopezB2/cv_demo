import pandas as pd

# Supongamos que tienes un diccionario de datos
data = {
    'Abbr Ejercicio': ['BarbellSquat'],
    
    'Hombro Derecho': ['34.5']
    
    
}

# Crea un DataFrame de pandas
df = pd.DataFrame(data)

# Guarda el DataFrame en un archivo CSV
df.to_csv('example.csv', index=False, sep=';')