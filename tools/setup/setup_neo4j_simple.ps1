# Script PowerShell para configurar Neo4j local con Docker MCP Toolkit
# Version simplificada sin emojis para evitar problemas de encoding

Write-Host "Configuracion de Neo4j Local con Docker MCP Toolkit" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host ""

# Variables
$NEO4J_URI = "bolt://localhost:7687"
$NEO4J_USER = "neo4j"
$NEO4J_PASSWORD = "password123"
$NEO4J_DATABASE = "neo4j"

# Verificar si Neo4j esta corriendo
Write-Host "Verificando si Neo4j local esta corriendo..." -ForegroundColor Yellow
$containers = docker ps --format "{{.Names}}"
$neo4jRunning = $containers -match "melquisedec-neo4j"

if ($neo4jRunning) {
    Write-Host "[OK] Neo4j local esta corriendo" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Neo4j local NO esta corriendo" -ForegroundColor Red
    Write-Host "Inicia con: docker-compose -f nucleo-investigacion/docker-compose.yml up -d neo4j" -ForegroundColor Yellow
    $response = Read-Host "Quieres iniciarlo ahora? (s/n)"
    if ($response -eq "s" -or $response -eq "S") {
        Write-Host "Iniciando Neo4j..." -ForegroundColor Cyan
        Set-Location nucleo-investigacion
        docker-compose up -d neo4j
        Set-Location ..
        Write-Host "Esperando 30 segundos..." -ForegroundColor Yellow
        Start-Sleep -Seconds 30
        $neo4jRunning = $true
    }
}

# Configurar neo4j-cypher
Write-Host ""
Write-Host "Configurando neo4j-cypher MCP..." -ForegroundColor Cyan

docker mcp config set neo4j-cypher NEO4J_URI $NEO4J_URI
Write-Host "[OK] NEO4J_URI configurado: $NEO4J_URI" -ForegroundColor Green

docker mcp config set neo4j-cypher NEO4J_DATABASE $NEO4J_DATABASE
Write-Host "[OK] NEO4J_DATABASE configurado: $NEO4J_DATABASE" -ForegroundColor Green

docker mcp secret set neo4j-cypher NEO4J_USER $NEO4J_USER
Write-Host "[OK] NEO4J_USER configurado" -ForegroundColor Green

docker mcp secret set neo4j-cypher NEO4J_PASSWORD $NEO4J_PASSWORD
Write-Host "[OK] NEO4J_PASSWORD configurado" -ForegroundColor Green

Write-Host "[OK] neo4j-cypher configurado correctamente" -ForegroundColor Green

# Configurar neo4j-memory
Write-Host ""
Write-Host "Configurando neo4j-memory MCP..." -ForegroundColor Cyan

docker mcp config set neo4j-memory NEO4J_URI $NEO4J_URI
Write-Host "[OK] NEO4J_URI configurado: $NEO4J_URI" -ForegroundColor Green

docker mcp config set neo4j-memory NEO4J_DATABASE "memory"
Write-Host "[OK] NEO4J_DATABASE configurado: memory" -ForegroundColor Green

docker mcp secret set neo4j-memory NEO4J_USER $NEO4J_USER
Write-Host "[OK] NEO4J_USER configurado" -ForegroundColor Green

docker mcp secret set neo4j-memory NEO4J_PASSWORD $NEO4J_PASSWORD
Write-Host "[OK] NEO4J_PASSWORD configurado" -ForegroundColor Green

Write-Host "[OK] neo4j-memory configurado correctamente" -ForegroundColor Green

# Crear base de datos memory si Neo4j esta corriendo
if ($neo4jRunning) {
    Write-Host ""
    Write-Host "Creando base de datos 'memory' en Neo4j..." -ForegroundColor Cyan
    
    try {
        $output = docker exec melquisedec-neo4j cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -d system "CREATE DATABASE memory IF NOT EXISTS;" 2>&1
        Write-Host "[OK] Base de datos 'memory' creada/verificada" -ForegroundColor Green
    } catch {
        Write-Host "[WARN] Error creando base de datos (puede que ya exista)" -ForegroundColor Yellow
    }
}

# Verificar configuracion
Write-Host ""
Write-Host "Verificando configuracion..." -ForegroundColor Cyan
Write-Host ""

Write-Host "Estado de servidores Neo4j:" -ForegroundColor Yellow
docker mcp server ls | Select-String "neo4j"

Write-Host ""
Write-Host "[OK] Configuracion completada!" -ForegroundColor Green
Write-Host ""
Write-Host "Proximos pasos:" -ForegroundColor Cyan
Write-Host "  1. Verifica que Neo4j este corriendo: docker ps"
Write-Host "  2. Prueba los MCPs: python nucleo-investigacion/scripts/test_docker_mcp_toolkit.py"
Write-Host "  3. Accede a Neo4j Browser: http://localhost:7474"
Write-Host "  4. Usuario: neo4j, Password: password123"
Write-Host "  5. Usa los MCPs en VS Code con GitHub Copilot"
Write-Host ""
