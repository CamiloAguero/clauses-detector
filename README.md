# ⚖️ Legal Clauses Detector (AI + Engineering)

> Un sistema inteligente que detecta cláusulas abusivas en contratos utilizando LLMs (Gemini 2.0 Flash) con una capa de validación estricta (Pydantic).

![CI Status](https://github.com/CamiloAguero/clauses-detector/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pydantic](https://img.shields.io/badge/Data%20Validation-Pydantic-red)
![UV](https://img.shields.io/badge/Package%20Manager-uv-purple)

## 💡 El Problema

La Inteligencia Artificial es excelente entendiendo lenguaje natural, pero **terrible siguiendo reglas estrictas**. En el mundo legal, una "alucinación" de la IA puede costar millones.

## 🛡️ La Solución (Arquitectura)

Este proyecto implementa una arquitectura de **"IA Domada"**:

1.  **Input:** Texto legal no estructurado.
2.  **Reasoning Engine:** Google Gemini Flash analiza semánticamente el riesgo.
3.  **Validation Layer:** `Pydantic` fuerza que la salida sea una estructura de datos válida, rechazando respuestas ambiguas o formatos incorrectos antes de que lleguen a la base de datos.
4.  **Safety:** Si la IA falla, el sistema captura el error y evita falsos positivos.

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.12
- **Gestor de Paquetes:** `uv` (Rust-based, ultra rápido)
- **IA:** Google Gemini 1.5 Flash (vía `google-generativeai`)
- **Validación:** Pydantic V2
- **Testing:** Pytest
- **CI/CD:** GitHub Actions

## 🚀 Cómo correrlo localmente

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/CamiloAguero/clauses-detector.git](https://github.com/CamiloAguero/clauses-detector.git)
    cd clauses-detector
    ```

2.  **Instalar dependencias (con uv):**

    ```bash
    uv sync
    ```

3.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` basado en el ejemplo:

    ```bash
    cp .env-example .env
    ```

    Y agrega tu `GOOGLE_API_KEY`.

4.  **Ejecutar el Detector:**

    ```bash
    uv run detector.py
    ```

5.  **Correr Tests:**
    ```bash
    uv run pytest
    ```

## 🤖 CI/CD Pipeline

Este proyecto cuenta con integración continua configurada en GitHub Actions.
Cada `push` a la rama `main` dispara:

- Instalación limpia del entorno con `uv`.
- Ejecución de Tests Unitarios (Validación de lógica Pydantic).
- _Nota: Los tests de integración con la API se saltan automáticamente en CI si no hay credenciales, garantizando seguridad._
