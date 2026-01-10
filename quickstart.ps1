# Quick Start Script para Triple-Persistence
# ===========================================

Write-Host "`n╔══════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  Triple-Persistence Quick Start                  ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check Docker
Write-Host "[1/5] Verificando Docker..." -ForegroundColor Yellow
try {
    $dockerVersion = docker --version
    Write-Host "✅ Docker OK: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker no instalado" -ForegroundColor Red
    Write-Host "   Descargar: https://www.docker.com/products/docker-desktop/" -ForegroundColor White
    exit 1
}

# Check Ollama
Write-Host "`n[2/5] Verificando Ollama..." -ForegroundColor Yellow
try {
    $ollamaModels = ollama list
    Write-Host "✅ Ollama OK" -ForegroundColor Green
} catch {
    Write-Host "❌ Ollama no instalado o no corriendo" -ForegroundColor Red
    Write-Host "   Descargar: https://ollama.ai/download" -ForegroundColor White
    exit 1
}

# Pull models
Write-Host "`n[3/5] Descargando modelos (si no existen)..." -ForegroundColor Yellow
Write-Host "   Modelo LLM (qwen2.5)..." -ForegroundColor Gray
ollama pull qwen2.5:latest
Write-Host "   Modelo embeddings (nomic-embed-text)..." -ForegroundColor Gray
ollama pull nomic-embed-text
Write-Host "✅ Modelos listos" -ForegroundColor Green

# Start GenAI Stack
Write-Host "`n[4/5] Iniciando GenAI Stack (Neo4j)..." -ForegroundColor Yellow
cd _lab\genai-stack
docker-compose up -d database
Write-Host "✅ Neo4j iniciando..." -ForegroundColor Green
Write-Host "   Espera 30 segundos para que inicie completamente" -ForegroundColor Gray

# Run examples
Write-Host "`n[5/5] Ejemplos disponibles:" -ForegroundColor Yellow
Write-Host ""
Write-Host "📚 LlamaIndex Examples:" -ForegroundColor Cyan
Write-Host "   cd packages\triple-persistence" -ForegroundColor White
Write-Host "   `$env:PYTHONIOENCODING='utf-8'; python examples\01_simple_ingestion.py" -ForegroundColor White
Write-Host "   `$env:PYTHONIOENCODING='utf-8'; python examples\02_vector_search.py" -ForegroundColor White
Write-Host "   `$env:PYTHONIOENCODING='utf-8'; python examples\03_graph_traversal.py" -ForegroundColor White
Write-Host ""
Write-Host "🌐 GenAI Stack Apps:" -ForegroundColor Cyan
Write-Host "   Neo4j Browser: " -NoNewline -ForegroundColor White
Write-Host "http://localhost:7474" -ForegroundColor Blue
Write-Host "   Chatbot: " -NoNewline -ForegroundColor White
Write-Host "docker-compose up -d bot; start http://localhost:8501" -ForegroundColor Blue
Write-Host "   PDF Bot: " -NoNewline -ForegroundColor White
Write-Host "docker-compose up -d pdf_bot; start http://localhost:8503" -ForegroundColor Blue
Write-Host ""
Write-Host "✅ Setup completado!" -ForegroundColor Green
Write-Host "   Ver manual: docs\guides\triple-persistence-quickstart.md" -ForegroundColor Gray
Write-Host ""
