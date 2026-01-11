# HYPATIA Knowledge Acquisition Setup Script
# SPEC-001: Built-in Template Spec Workflow
# Fecha: 2026-01-10

Write-Host "[HYPATIA] Knowledge Acquisition Setup" -ForegroundColor Cyan
Write-Host "=" * 60

# 1. Verificar Ollama
Write-Host "`n[1/4] Verificando Ollama..." -ForegroundColor Yellow
if (Get-Command ollama -ErrorAction SilentlyContinue) {
    Write-Host "  ✅ Ollama ya está instalado" -ForegroundColor Green
    ollama --version
} else {
    Write-Host "  ❌ Ollama no está instalado" -ForegroundColor Red
    Write-Host "  Descargando Ollama para Windows..." -ForegroundColor Yellow
    
    $ollamaUrl = "https://ollama.com/download/OllamaSetup.exe"
    $installerPath = "$env:TEMP\OllamaSetup.exe"
    
    try {
        Invoke-WebRequest -Uri $ollamaUrl -OutFile $installerPath
        Write-Host "  ✅ Descarga completada" -ForegroundColor Green
        Write-Host "  🚀 Ejecutando instalador..." -ForegroundColor Yellow
        Start-Process -FilePath $installerPath -Wait
        Write-Host "  ✅ Ollama instalado" -ForegroundColor Green
    } catch {
        Write-Host "  ❌ Error descargando Ollama: $_" -ForegroundColor Red
        Write-Host "  Por favor instala manualmente desde: https://ollama.com/download" -ForegroundColor Yellow
        exit 1
    }
}

# 2. Descargar modelo nomic-embed-text
Write-Host "`n[2/4] Descargando modelo nomic-embed-text (768 dimensiones)..." -ForegroundColor Yellow
try {
    ollama pull nomic-embed-text
    Write-Host "  ✅ Modelo nomic-embed-text descargado" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Error descargando modelo: $_" -ForegroundColor Red
    exit 1
}

# 3. Verificar Neo4j
Write-Host "`n[3/4] Verificando Neo4j..." -ForegroundColor Yellow
$neo4jContainers = docker ps -a --filter "name=neo4j" --format "{{.Names}}"
if ($neo4jContainers) {
    Write-Host "  ✅ Contenedores Neo4j encontrados:" -ForegroundColor Green
    $neo4jContainers | ForEach-Object { Write-Host "    - $_" }
    
    Write-Host "`n  🚀 Iniciando contenedor melquisedec-neo4j..." -ForegroundColor Yellow
    docker start melquisedec-neo4j
    
    Start-Sleep -Seconds 5
    Write-Host "  ✅ Neo4j iniciado" -ForegroundColor Green
    Write-Host "  🌐 Acceso: http://localhost:7474" -ForegroundColor Cyan
    Write-Host "  🔐 Credenciales: neo4j/password" -ForegroundColor Cyan
} else {
    Write-Host "  ⚠️  No se encontraron contenedores Neo4j" -ForegroundColor Yellow
    Write-Host "  Creando nuevo contenedor..." -ForegroundColor Yellow
    
    docker run -d `
        --name hypatia-neo4j `
        -p 7474:7474 `
        -p 7687:7687 `
        -e NEO4J_AUTH=neo4j/password `
        -e NEO4J_PLUGINS='["apoc", "graph-data-science"]' `
        neo4j:5.15
    
    Start-Sleep -Seconds 10
    Write-Host "  ✅ Neo4j creado e iniciado" -ForegroundColor Green
    Write-Host "  🌐 Acceso: http://localhost:7474" -ForegroundColor Cyan
}

# 4. Instalar dependencias Python
Write-Host "`n[4/4] Instalando dependencias Python..." -ForegroundColor Yellow
$pythonPackages = @(
    "langchain",
    "langchain-community",
    "pypdf2",
    "pdfplumber",
    "neo4j",
    "ollama",
    "semanticscholar",
    "numpy",
    "scikit-learn"
)

pip install $pythonPackages -q
Write-Host "  ✅ Dependencias Python instaladas" -ForegroundColor Green

# 5. Crear directorio temporal para descargas
Write-Host "`n[FINAL] Verificando estructura de directorios..." -ForegroundColor Yellow
$baseDir = $PSScriptRoot
$dirs = @("literature/ddd", "literature/iso", "literature/imrad", "literature/spec-workflow-mcp", 
          "concepts", "frameworks", "embeddings", "graphs")

foreach ($dir in $dirs) {
    $fullPath = Join-Path $baseDir $dir
    if (!(Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
    }
}
Write-Host "  ✅ Estructura de directorios verificada" -ForegroundColor Green

# 6. Resumen
Write-Host "`n" + ("=" * 60)
Write-Host "[OK] HYPATIA Setup Completado" -ForegroundColor Green
Write-Host "`n[NEXT] Siguiente paso:" -ForegroundColor Cyan
Write-Host "  Ejecuta: python hypatia_acquire.py" -ForegroundColor White
Write-Host "`n[SOURCES] Fuentes a descargar:" -ForegroundColor Cyan
Write-Host "  - DDD: Evans (2003), Vernon (2013)" -ForegroundColor White
Write-Host "  - ISO: 21838-1:2019, 21838-2:2019" -ForegroundColor White
Write-Host "  - IMRAD: Sollaci & Pereira (2004)" -ForegroundColor White
Write-Host "  - Código: spec-workflow-mcp repository" -ForegroundColor White
Write-Host ""
