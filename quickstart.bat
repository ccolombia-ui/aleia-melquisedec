@echo off
REM Quick Start Script para Triple-Persistence
REM ===========================================

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║  Triple-Persistence Quick Start                  ║
echo ╚══════════════════════════════════════════════════╝
echo.

REM Check Docker
echo [1/5] Verificando Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker no instalado
    echo    Descargar: https://www.docker.com/products/docker-desktop/
    exit /b 1
)
echo ✅ Docker OK

REM Check Ollama
echo [2/5] Verificando Ollama...
ollama list >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Ollama no instalado o no corriendo
    echo    Descargar: https://ollama.ai/download
    exit /b 1
)
echo ✅ Ollama OK

REM Pull models
echo [3/5] Descargando modelos (si no existen)...
ollama pull qwen2.5:latest
ollama pull nomic-embed-text
echo ✅ Modelos listos

REM Start GenAI Stack
echo [4/5] Iniciando GenAI Stack (Neo4j)...
cd _lab\genai-stack
docker-compose up -d database
echo ✅ Neo4j iniciando...
echo    Espera 30 segundos para que inicie completamente

REM Run examples
echo [5/5] Ejemplos disponibles:
echo.
echo 📚 LlamaIndex Examples:
echo    cd packages\triple-persistence
echo    python examples\01_simple_ingestion.py
echo    python examples\02_vector_search.py
echo    python examples\03_graph_traversal.py
echo.
echo 🌐 GenAI Stack Apps:
echo    Neo4j Browser: http://localhost:7474
echo    Chatbot: docker-compose up -d bot ^& start http://localhost:8501
echo    PDF Bot: docker-compose up -d pdf_bot ^& start http://localhost:8503
echo.
echo ✅ Setup completado!
echo    Ver manual: docs\guides\triple-persistence-quickstart.md
echo.
pause
