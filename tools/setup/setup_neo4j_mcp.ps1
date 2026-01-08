# Script PowerShell para configurar Neo4j local con Docker MCP Toolkit
# Este script conecta tu Neo4j local (docker-compose) con los MCPs de Docker Toolkit

Write-Host "🔧 Configuración de Neo4j Local con Docker MCP Toolkit" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Variables
$NEO4J_URI = "bolt://localhost:7687"
$NEO4J_USER = "neo4j"
$NEO4J_PASSWORD = "password123"
$NEO4J_DATABASE = "neo4j"

# Función para verificar si docker-compose está corriendo
function Test-Neo4jRunning {
    Write-Host "📡 Verificando si Neo4j local está corriendo..." -ForegroundColor Yellow
    $containers = docker ps --format "{{.Names}}"
    if ($containers -match "melquisedec-neo4j") {
        Write-Host "✅ Neo4j local está corriendo" -ForegroundColor Green
        return $true
    } else {
        Write-Host "❌ Neo4j local NO está corriendo" -ForegroundColor Red
        Write-Host "   Inicia con: docker-compose up -d neo4j" -ForegroundColor Yellow
        return $false
    }
}

# Función para configurar neo4j-cypher
function Configure-Neo4jCypher {
    Write-Host ""
    Write-Host "🔧 Configurando neo4j-cypher MCP..." -ForegroundColor Cyan

    # Configurar URI
    docker mcp config set neo4j-cypher NEO4J_URI $NEO4J_URI
    Write-Host "  ✅ NEO4J_URI configurado: $NEO4J_URI" -ForegroundColor Green

    # Configurar DATABASE
    docker mcp config set neo4j-cypher NEO4J_DATABASE $NEO4J_DATABASE
    Write-Host "  ✅ NEO4J_DATABASE configurado: $NEO4J_DATABASE" -ForegroundColor Green

    # Configurar secretos
    docker mcp secret set neo4j-cypher NEO4J_USER $NEO4J_USER
    Write-Host "  ✅ NEO4J_USER configurado" -ForegroundColor Green

    docker mcp secret set neo4j-cypher NEO4J_PASSWORD $NEO4J_PASSWORD
    Write-Host "  ✅ NEO4J_PASSWORD configurado" -ForegroundColor Green

    Write-Host "✅ neo4j-cypher configurado correctamente" -ForegroundColor Green
}

# Función para configurar neo4j-memory
function Configure-Neo4jMemory {
    Write-Host ""
    Write-Host "🔧 Configurando neo4j-memory MCP..." -ForegroundColor Cyan

    # Configurar URI
    docker mcp config set neo4j-memory NEO4J_URI $NEO4J_URI
    Write-Host "  ✅ NEO4J_URI configurado: $NEO4J_URI" -ForegroundColor Green

    # Configurar DATABASE (memoria usa database 'memory')
    docker mcp config set neo4j-memory NEO4J_DATABASE "memory"
    Write-Host "  ✅ NEO4J_DATABASE configurado: memory" -ForegroundColor Green

    # Configurar secretos
    docker mcp secret set neo4j-memory NEO4J_USER $NEO4J_USER
    Write-Host "  ✅ NEO4J_USER configurado" -ForegroundColor Green

    docker mcp secret set neo4j-memory NEO4J_PASSWORD $NEO4J_PASSWORD
    Write-Host "  ✅ NEO4J_PASSWORD configurado" -ForegroundColor Green

    Write-Host "✅ neo4j-memory configurado correctamente" -ForegroundColor Green
}

# Función para crear base de datos memory en Neo4j
# Función para crear base de datos memory en Neo4j
function Create-MemoryDatabase {
    Write-Host ""
    Write-Host "🗄️  Creando base de datos 'memory' en Neo4j..." -ForegroundColor Cyan

    $cypher = "CREATE DATABASE memory IF NOT EXISTS;"

    try {
        $result = docker exec melquisedec-neo4j cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -d system $cypher 2>&1
        Write-Host "✅ Base de datos 'memory' creada" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Error creando base de datos (puede que ya exista): $_" -ForegroundColor Yellow
    }
}

# Función para configurar redis (si lo usas para embeddings)
function Configure-Redis {
    Write-Host ""
    Write-Host "🔧 Configurando redis MCP..." -ForegroundColor Cyan
    Write-Host "⚠️  Redis requiere una instancia corriendo" -ForegroundColor Yellow
    Write-Host "   Puedes agregarlo al docker-compose.yml si lo necesitas" -ForegroundColor Yellow

    $response = Read-Host "¿Quieres configurar Redis? (s/n)"
    if ($response -eq "s" -or $response -eq "S") {
        docker mcp config set redis REDIS_URI "redis://localhost:6379"
        docker mcp config set redis REDIS_DB "0"
        Write-Host "✅ Redis configurado para localhost:6379" -ForegroundColor Green
    } else {
        Write-Host "⏭️  Redis omitido" -ForegroundColor Yellow
    }
}

# Función para verificar configuración
function Show-Configuration {
    Write-Host ""
    Write-Host "🔍 Verificando configuración..." -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Estado de servidores Neo4j:" -ForegroundColor Yellow
    docker mcp server ls | Select-String "neo4j"

    Write-Host ""
    Write-Host "✅ Configuración completada!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📝 Próximos pasos:" -ForegroundColor Cyan
    Write-Host "   1. Verifica que Neo4j esté corriendo: docker ps"
    Write-Host "   2. Prueba los MCPs: python scripts/test_docker_mcp_toolkit.py"
    Write-Host "   3. Accede a Neo4j Browser: http://localhost:7474"
    Write-Host "   4. Usa los MCPs en VS Code con GitHub Copilot"
    Write-Host ""
}

# Main
function Main {
    # Verificar Neo4j
    $neo4jRunning = Test-Neo4jRunning

    if (-not $neo4jRunning) {
        Write-Host ""
        $response = Read-Host "¿Quieres iniciar Neo4j ahora? (s/n)"
        if ($response -eq "s" -or $response -eq "S") {
            Write-Host "🚀 Iniciando Neo4j..." -ForegroundColor Cyan
            docker-compose up -d neo4j
            Write-Host "⏳ Esperando que Neo4j esté listo (30s)..." -ForegroundColor Yellow
            Start-Sleep -Seconds 30
            $neo4jRunning = $true
        } else {
            Write-Host "⚠️  Continúa la configuración sin verificar Neo4j" -ForegroundColor Yellow
        }
    }

    # Configurar MCPs
    Configure-Neo4jCypher
    Configure-Neo4jMemory

    # Crear base de datos memory si Neo4j está corriendo
    if ($neo4jRunning) {
        Create-MemoryDatabase
    }

    Configure-Redis

    # Verificar
    Show-Configuration
}

# Ejecutar
Main
