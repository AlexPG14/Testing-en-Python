

# Mi función en src/math_utils.py
def calcular_promedio(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)

# Mi test en tests/test_math.py
def test_calcular_promedio():
    # Arrange
    ventas = [10, 20, 30]
    # Act
    resultado = calcular_promedio(ventas)
    # Assert
    assert resultado == 20.0

def test_calcular_promedio_lista_vacia():
    assert calcular_promedio([]) == 0




import pandas as pd

# Función que limpia un dataset
def limpiar_datos_ventas(df):
    # Elimina filas con precios nulos y filtra ventas negativas
    df_limpio = df.dropna(subset=['precio'])
    df_limpio = df_limpio[df_limpio['precio'] > 0]
    return df_limpio

# Testeando el DataFrame
def test_limpiar_datos_ventas():
    # Arrange: Creamos un mini-dataframe controlado
    datos_crudos = pd.DataFrame({
        'id_venta': [1, 2, 3],
        'precio': [100, None, -50] # Un dato bueno, un nulo, un negativo
    })
    
    # Act
    df_resultado = limpiar_datos_ventas(datos_crudos)
    
    # Assert
    assert len(df_resultado) == 1 # Solo debe quedar 1 fila
    assert df_resultado.iloc[0]['id_venta'] == 1 # Debe ser el ID 1