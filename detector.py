import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from pydantic import Field, ValidationError, BaseModel

# Configuración de Seguridad
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

# Validación si hay api key
if api_key:
    genai.configure(api_key=api_key)

# Modelo de datos
class Analisisclausula(BaseModel):
    es_abusiva: bool = Field(..., description="True si la claúsula es injusta o ilegal, False si es normal")
    nivel_riesgo: str = Field(..., description="Nivel de severidad: Bajo, Medio, Alto")
    explicacion: str = Field(..., description="Breve explicación jurídica de por qué es o no abusiva")

# Función principal
def analizar_texto_legal(texto_clausula: str) -> dict:
    """
    Toma un texto legal y usa IA para determinar si es abusivo.
    Devuelve un diccionario validado o un error.
    """
    # Validación de api key
    if not api_key:
        return {"error": "Falta la API Key en el archivo .env"}
    
    # El Prompt del sistema
    system_prompt = """
    Eres un abogado auditor experto en derechos del consumidor y laboral.
    Analiza la cláusula entregada.
    Tu salida debe ser un JSON estricto que cumpla con este esquema:
    {
        "es_abusiva": bool,
        "nivel_riesgo": "Bajo" | "Medio" | "Alto",
        "explicacion": "string"
    }
    """

    try:
        model = genai.GenerativeModel(
            "gemini-flash-latest",
            system_instruction=system_prompt,
            generation_config={'response_mime_type': 'application/json'}
        )

        # Envío de la clausula
        response = model.generate_content(texto_clausula)

        # Parseo a JSON
        datos_json = json.loads(response.text)

        # Validación por Pydantic
        analisis = Analisisclausula(**datos_json)

        # Retornar diccionario limpio
        return analisis.model_dump()
    
    except Exception as e:
        return {"error": f"Error procesando la cláusula: {str(e)}"}
    
if __name__ == "__main__":
    # Clausula abusiva
    clausula = "El empleado deberá pagar una multa de 100 millones de pesos si renuncia antes de 50 años."

    print(f"🧐 Analizando: '{clausula}'...")
    resultado = analizar_texto_legal(clausula)

    # Imprimir el JSON formateado
    print(json.dumps(resultado, indent=2, ensure_ascii=False))