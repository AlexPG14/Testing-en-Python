import pytest
import pandas as pd
import numpy as np
from penguin_processor import limpiar_especies, calcular_bmi, filtrar_datos_validos

@pytest.fixture
def datos_ejemplo():
    """Crea un pequeño DataFrame con la estructura del CSV de pingüinos."""
    return pd.DataFrame({
        'Species': ['Adelie Penguin (Pygoscelis adeliae)', 'Gentoo penguin (Pygoscelis papua)'],
        'Body Mass (g)': [3750, 5000],
        'Flipper Length (mm)': [181, 210],
        'Sex': ['MALE', np.nan]
    })

def test_limpiar_especies(datos_ejemplo):
    df_result = limpiar_especies(datos_ejemplo)
    assert df_result['Species'].iloc[0] == 'Adelie'

def test_calcular_bmi(datos_ejemplo):
    df_result = calcular_bmi(datos_ejemplo)
    assert 'bmi' in df_result.columns
    assert round(df_result['bmi'].iloc[0], 2) == 20.72

def test_filtrar_datos_validos(datos_ejemplo):
   
    df_result = filtrar_datos_validos(datos_ejemplo)
    assert len(df_result) == 1