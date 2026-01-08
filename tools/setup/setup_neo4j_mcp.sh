#!/bin/bash
# Script para configurar Neo4j local con Docker MCP Toolkit
# Este script conecta tu Neo4j local (docker-compose) con los MCPs de Docker Toolkit

set -e

echo "🔧 Configuración de Neo4j Local con Docker MCP Toolkit"
echo "========================================================"
echo ""

# Variables
NEO4J_URI="bolt://localhost:7687"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="password123"
NEO4J_DATABASE="neo4j"

# Función para verificar si docker-compose está corriendo
check_neo4j_running() {
    echo "📡 Verificando si Neo4j local está corriendo..."
    if docker ps | grep -q "melquisedec-neo4j"; then
        echo "✅ Neo4j local está corriendo"
        return 0
    else
        echo "❌ Neo4j local NO está corriendo"
        echo "   Inicia con: docker-compose up -d neo4j"
        return 1
    fi
}

# Función para configurar neo4j-cypher
configure_neo4j_cypher() {
    echo ""
    echo "🔧 Configurando neo4j-cypher MCP..."

    # Configurar URI
    docker mcp config set neo4j-cypher NEO4J_URI "$NEO4J_URI"
    echo "  ✅ NEO4J_URI configurado: $NEO4J_URI"

    # Configurar DATABASE
    docker mcp config set neo4j-cypher NEO4J_DATABASE "$NEO4J_DATABASE"
    echo "  ✅ NEO4J_DATABASE configurado: $NEO4J_DATABASE"

    # Configurar secretos
    docker mcp secret set neo4j-cypher NEO4J_USER "$NEO4J_USER"
    echo "  ✅ NEO4J_USER configurado"

    docker mcp secret set neo4j-cypher NEO4J_PASSWORD "$NEO4J_PASSWORD"
    echo "  ✅ NEO4J_PASSWORD configurado"

    echo "✅ neo4j-cypher configurado correctamente"
}

# Función para configurar neo4j-memory
configure_neo4j_memory() {
    echo ""
    echo "🔧 Configurando neo4j-memory MCP..."

    # Configurar URI
    docker mcp config set neo4j-memory NEO4J_URI "$NEO4J_URI"
    echo "  ✅ NEO4J_URI configurado: $NEO4J_URI"

    # Configurar DATABASE (memoria usa database 'memory')
    docker mcp config set neo4j-memory NEO4J_DATABASE "memory"
    echo "  ✅ NEO4J_DATABASE configurado: memory"

    # Configurar secretos
    docker mcp secret set neo4j-memory NEO4J_USER "$NEO4J_USER"
    echo "  ✅ NEO4J_USER configurado"

    docker mcp secret set neo4j-memory NEO4J_PASSWORD "$NEO4J_PASSWORD"
    echo "  ✅ NEO4J_PASSWORD configurado"

    echo "✅ neo4j-memory configurado correctamente"
}

# Función para configurar redis (si lo usas para embeddings)
configure_redis() {
    echo ""
    echo "🔧 Configurando redis MCP..."
    echo "⚠️  Redis requiere una instancia corriendo"
    echo "   Puedes agregarlo al docker-compose.yml si lo necesitas"

    read -p "¿Quieres configurar Redis? (s/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        docker mcp config set redis REDIS_URI "redis://localhost:6379"
        docker mcp config set redis REDIS_DB "0"
        echo "✅ Redis configurado para localhost:6379"
    else
        echo "⏭️  Redis omitido"
    fi
}

# Función para verificar configuración
verify_configuration() {
    echo ""
    echo "🔍 Verificando configuración..."
    echo ""

    echo "Estado de servidores Neo4j:"
    docker mcp server ls | grep "neo4j"

    echo ""
    echo "✅ Configuración completada!"
    echo ""
    echo "📝 Próximos pasos:"
    echo "   1. Verifica que Neo4j esté corriendo: docker ps"
    echo "   2. Prueba los MCPs: python scripts/test_docker_mcp_toolkit.py"
    echo "   3. Accede a Neo4j Browser: http://localhost:7474"
    echo "   4. Usa los MCPs en VS Code con GitHub Copilot"
}

# Main
main() {
    # Verificar Neo4j
    if ! check_neo4j_running; then
        echo ""
        read -p "¿Quieres iniciar Neo4j ahora? (s/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
            echo "🚀 Iniciando Neo4j..."
            docker-compose up -d neo4j
            echo "⏳ Esperando que Neo4j esté listo (30s)..."
            sleep 30
        else
            echo "⚠️  Continúa la configuración sin verificar Neo4j"
        fi
    fi

    # Configurar MCPs
    configure_neo4j_cypher
    configure_neo4j_memory
    configure_redis

    # Verificar
    verify_configuration
}

# Ejecutar
main
