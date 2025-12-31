import pytest
import os
from pydantic import ValidationError
from detector import Analisisclausula, analizar_texto_legal

# TEST 1: Lógica de validación
def test_modelo_pydantic_valido():
    datos = {
        "es_abusiva": True,
        "nivel_riesgo": "Alto",
        "explicacion": "Texto de prueba"
    }
    modelo = Analisisclausula(**datos)
    assert modelo.es_abusiva is True
    assert modelo.nivel_riesgo == "Alto"

# TEST 2: Validación de errores
def test_modelo_pydantic_invalido():
    datos_malos = {
        "es_abusiva": "No sé",
        "nivel_riesgo": "Alto"
    }
    # Esperando a que falle
    with pytest.raises(ValidationError):
        Analisisclausula(**datos_malos)

# TEST 3: Integración genai
@pytest.mark.skipif(os.getenv('GOOGLE_API_KEY') is None, reason="No hay API Key configurada en este entorno")
def test_lamada_api_real():
    clausula = "El usuario renunca a todos sus derechos humanos."
    resultado = analizar_texto_legal(clausula)

    # Verificar que responda lo que debe
    assert "es_abusiva" in resultado
    assert resultado["es_abusiva"] is True