import pandas as pd
import numpy as np

def limpiar_especies(df):
    """
    Simplifica el nombre de la especie. 
    Ej: 'Adelie Penguin (Pygoscelis adeliae)' -> 'Adelie'
    """
   
    df['Species'].str.split(',').str[0]
    return df

def calcular_bmi(df):
    """
    Calcula el BMI simple: masa_g / (flipper_length_mm)
    """
   
    df['bmi'] = df['Body Mass (g)'] / df['Flipper Length (mm)']
    return df

def filtrar_datos_validos(df):
    """Elimina filas donde el sexo es desconocido o nulo."""
   
    return df.dropna(subset=['Sex'])