# Guía Completa: Docker MCP Toolkit + Neo4j Local

**Fecha:** 2026-01-07  
**Propósito:** Conectar Neo4j local con Docker MCP Toolkit para gestionar grafos y embeddings

---

## 📋 Índice

1. [Arquitectura del Sistema](#arquitectura)
2. [Configuración de Neo4j Local](#configuracion-neo4j)
3. [Métricas y Explicación](#metricas)
4. [Scripts de Prueba](#scripts)
5. [Uso Práctico](#uso-practico)
6. [Troubleshooting](#troubleshooting)

---

## 🏗️ Arquitectura del Sistema {#arquitectura}

### Componentes Principales

```
┌─────────────────────────────────────────────────────────┐
│                   VS Code + GitHub Copilot              │
│                                                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │           Docker MCP Toolkit Gateway              │ │
│  │         (docker mcp gateway run)                  │ │
│  └───────────────┬───────────────────────────────────┘ │
└──────────────────┼─────────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
┌───────▼────────┐   ┌────────▼──────────┐
│ Neo4j MCPs     │   │ Otros MCPs        │
│ ├─cypher       │   │ ├─wikipedia       │
│ ├─memory       │   │ ├─context7        │
│ └─modeling     │   │ ├─firecrawl       │
└────────┬───────┘   │ └─perplexity      │
         │           └───────────────────┘
         │
┌────────▼─────────────────────────────┐
│    Docker Compose (Local)            │
│  ┌────────────────────────────────┐  │
│  │  Neo4j 5.15 Community          │  │
│  │  └─ bolt://localhost:7687      │  │
│  │  └─ http://localhost:7474      │  │
│  └────────────────────────────────┘  │
│  ┌────────────────────────────────┐  │
│  │  Ollama                        │  │
│  │  └─ embeddings: nomic-embed    │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
```

### Flujo de Datos

1. **Usuario** → Interactúa con GitHub Copilot en VS Code
2. **Copilot** → Se conecta al `MCP_DOCKER` gateway
3. **Gateway** → Enruta solicitudes a servidores MCP específicos
4. **MCP Neo4j** → Se conecta a Neo4j local (localhost:7687)
5. **Neo4j** → Almacena/consulta grafos de conocimiento
6. **Ollama** → Genera embeddings para búsquedas semánticas

---

## ⚙️ Configuración de Neo4j Local {#configuracion-neo4j}

### 1. Docker Compose Mejorado

El archivo `docker-compose.yml` ahora incluye:

```yaml
neo4j:
  image: neo4j:5.15-community
  container_name: melquisedec-neo4j
  ports:
    - "7474:7474"   # Neo4j Browser
    - "7687:7687"   # Bolt protocol
  environment:
    # Autenticación
    - NEO4J_AUTH=neo4j/password123
    
    # Memoria optimizada para embeddings
    - NEO4J_dbms_memory_heap_initial__size=512M
    - NEO4J_dbms_memory_heap_max__size=2G
    - NEO4J_dbms_memory_pagecache_size=512M
    
    # Plugins para grafos de conocimiento
    - NEO4J_PLUGINS=["apoc", "graph-data-science"]
    - NEO4J_dbms_security_procedures_unrestricted=apoc.*,gds.*
    
    # Red
    - NEO4J_dbms_connector_bolt_advertised__address=localhost:7687
  volumes:
    - neo4j_data:/data           # Persistencia de datos
    - neo4j_logs:/logs           # Logs para debugging
    - neo4j_import:/import       # Importar CSVs/datos
    - neo4j_plugins:/plugins     # Plugins adicionales
  healthcheck:
    test: ["CMD-SHELL", "cypher-shell -u neo4j -p password123 'RETURN 1'"]
    interval: 10s
    timeout: 5s
    retries: 5
```

### 2. Características Neo4j Mejoradas

#### **Memoria Optimizada**
- **Heap inicial:** 512MB (arranque rápido)
- **Heap máximo:** 2GB (operaciones complejas)
- **Page cache:** 512MB (consultas rápidas)

#### **Plugins Instalados**
- **APOC:** Procedimientos y funciones avanzadas
- **Graph Data Science:** Algoritmos de grafos (PageRank, similitud, etc.)

#### **Bases de Datos**
- **neo4j:** Base de datos principal para grafos de conocimiento
- **memory:** Base de datos dedicada para memoria persistente de IA

### 3. Configurar MCPs con Neo4j Local

Ejecuta el script de configuración:

```powershell
# Windows PowerShell
.\scripts\setup_neo4j_mcp.ps1

# O en bash (WSL/Linux/Mac)
bash scripts/setup_neo4j_mcp.sh
```

El script configura automáticamente:
- ✅ `neo4j-cypher` → Para consultas Cypher
- ✅ `neo4j-memory` → Para memoria persistente
- ✅ Crea base de datos `memory`
- ✅ Verifica conectividad

### 4. Configuración Manual (alternativa)

```powershell
# Neo4j Cypher MCP
docker mcp config set neo4j-cypher NEO4J_URI "bolt://localhost:7687"
docker mcp config set neo4j-cypher NEO4J_DATABASE "neo4j"
docker mcp secret set neo4j-cypher NEO4J_USER "neo4j"
docker mcp secret set neo4j-cypher NEO4J_PASSWORD "password123"

# Neo4j Memory MCP
docker mcp config set neo4j-memory NEO4J_URI "bolt://localhost:7687"
docker mcp config set neo4j-memory NEO4J_DATABASE "memory"
docker mcp secret set neo4j-memory NEO4J_USER "neo4j"
docker mcp secret set neo4j-memory NEO4J_PASSWORD "password123"
```

---

## 📊 Métricas y Explicación {#metricas}

### Métricas del Sistema

El script `test_docker_mcp_toolkit.py` genera las siguientes métricas:

#### **1. Total Habilitados**
- **Qué es:** Número de servidores MCP activos en Docker Toolkit
- **Cómo se habilitan:** `docker mcp server enable <nombre>`
- **Ejemplo:** Si tienes 19 servidores habilitados, este número es 19
- **Por qué importa:** Indica la cantidad de herramientas disponibles para Copilot

#### **2. Con Secretos Configurados (✓ done)**
- **Qué es:** Servidores con API keys/tokens configurados
- **Cómo se configuran:** `docker mcp secret set <server> <key> <value>`
- **Ejemplo:** `brave` necesita `BRAVE_API_KEY`
- **Por qué importa:** Sin secretos, el servidor no puede autenticarse con servicios externos
- **Estado visual:** ✓ done (verde) = configurado

#### **3. Con Configuración (✓ done)**
- **Qué es:** Servidores con parámetros adicionales configurados
- **Cómo se configuran:** `docker mcp config set <server> <key> <value>`
- **Ejemplo:** Neo4j necesita `NEO4J_URI`, `NEO4J_DATABASE`
- **Por qué importa:** Define cómo el MCP se conecta a servicios
- **Estado visual:** ✓ done (verde) = configurado

#### **4. Requieren Secretos (▲ required)**
- **Qué es:** Servidores que NO funcionarán sin API keys
- **Estado visual:** ▲ required (rojo) = bloqueante
- **Ejemplo:** `redis` necesita URI antes de funcionar
- **Acción necesaria:** Configurar secretos antes de usar

#### **5. Requieren Configuración (▲ required)**
- **Qué es:** Servidores que necesitan parámetros obligatorios
- **Estado visual:** ▲ required (rojo) = bloqueante
- **Ejemplo:** `neo4j-data-modeling` necesita configuración de rutas
- **Acción necesaria:** Completar configuración antes de usar

#### **6. Tasa de Éxito**
- **Qué es:** Porcentaje de MCPs que responden correctamente
- **Fórmula:** `(MCPs exitosos / MCPs probados) × 100`
- **Ejemplo:** 15 exitosos de 17 probados = 88.2%
- **Por qué importa:** Indica salud general del sistema MCP

#### **7. Completitud de Configuración**
- **Qué es:** Porcentaje de configuración completa
- **Fórmula:** `((Con secretos + Con config) / (Total × 2)) × 100`
- **Ejemplo:** Si 10 de 19 tienen secretos y 12 tienen config = 57.9%
- **Por qué importa:** Muestra cuánto falta para completar la configuración

### Símbolos de Estado

```
✓ done      → Configurado correctamente (verde)
◐ partial   → Parcialmente configurado (amarillo)
▲ required  → Requiere configuración (rojo)
-           → No aplica o no necesario
```

### Interpretación de Resultados

#### **Escenario 1: Todo Verde**
```
Total: 19 servidores
Con secretos: 15 ✓
Con config: 18 ✓
Tasa de éxito: 95%
```
**Interpretación:** Sistema bien configurado, listo para producción

#### **Escenario 2: Algunos Rojos**
```
Total: 19 servidores
Requieren secretos: 4 ▲
Requieren config: 2 ▲
Tasa de éxito: 68%
```
**Interpretación:** Funcional pero incompleto, configurar los rojos

#### **Escenario 3: Muchos Rojos**
```
Total: 19 servidores
Requieren secretos: 10 ▲
Tasa de éxito: 47%
```
**Interpretación:** Configuración inicial, completar secretos urgente

---

## 🧪 Scripts de Prueba {#scripts}

### 1. test_docker_mcp_toolkit.py

**Propósito:** Prueba exhaustiva de todos los MCPs de Docker Toolkit

**Características:**
- ✅ Lista todos los servidores MCP habilitados
- ✅ Valida secretos y configuración
- ✅ Verifica conectividad básica
- ✅ Genera métricas detalladas
- ✅ Exporta resultados a JSON
- ✅ Colores ANSI para mejor legibilidad

**Uso:**
```powershell
# Prueba básica
python scripts/test_docker_mcp_toolkit.py

# Con modo verbose
python scripts/test_docker_mcp_toolkit.py --verbose

# Con timeout personalizado
python scripts/test_docker_mcp_toolkit.py --timeout 30 -v
```

**Salida:**
```
🚀 DOCKER MCP TOOLKIT - PRUEBA DE SERVIDORES
============================================================

🔍 Verificando Docker MCP Toolkit...
✅ Docker MCP Toolkit disponible

📋 Listando servidores MCP...
✅ 19 servidores MCP encontrados

🧪 Probando servidores...

🔧 Probando: arxiv-mcp-server
  ✅ Detalles obtenidos
  ✅ Disponible

[... más pruebas ...]

📊 REPORTE DE MÉTRICAS - DOCKER MCP TOOLKIT
============================================================

Servidores:
  Total habilitados: 19
  Con secretos configurados: 15
  Con configuración: 16
  Requieren secretos: 2
  Requieren configuración: 1

Pruebas:
  Probados: 17
  ✅ Exitosos: 15
  ❌ Fallidos: 0
  ⏭️  Omitidos: 2

Tasa de éxito: 88.2%
Completitud de configuración: 81.6%
```

### 2. test_mcps.py (Original)

**Propósito:** Prueba MCPs configurados en `.vscode/mcp.json`

**Cuándo usarlo:**
- Para probar configuraciones locales de Claude Desktop
- Para validar configuración manual en `.vscode/mcp.json`
- Para proyectos sin Docker MCP Toolkit

**Diferencias con test_docker_mcp_toolkit.py:**

| Característica | test_mcps.py | test_docker_mcp_toolkit.py |
|---------------|--------------|---------------------------|
| **Fuente** | `.vscode/mcp.json` | Docker MCP Toolkit |
| **Comando** | Ejecuta binarios | Usa `docker mcp` CLI |
| **Scope** | Proyecto local | Sistema global |
| **Env vars** | Lee de `.env` | Lee de Docker secrets |
| **Validación** | `--version`, `--help` | Estado del servidor |

---

## 🎯 Uso Práctico {#uso-practico}

### Caso de Uso 1: Grafo de Conocimiento

**Objetivo:** Almacenar y consultar conocimiento estructurado

```cypher
// Crear nodos de conceptos
CREATE (a:Concepto {nombre: "Docker MCP Toolkit", tipo: "Tecnología"})
CREATE (b:Concepto {nombre: "Neo4j", tipo: "Base de Datos"})
CREATE (c:Concepto {nombre: "GitHub Copilot", tipo: "IA"})

// Crear relaciones
CREATE (c)-[:USA]->(a)
CREATE (a)-[:CONECTA_A]->(b)
CREATE (b)-[:ALMACENA]->(d:Dato {tipo: "Grafo de Conocimiento"})
```

**Usar con Copilot:**
```
@workspace "Usando neo4j-cypher MCP, busca todos los conceptos 
relacionados con 'Docker MCP Toolkit' en el grafo de conocimiento"
```

### Caso de Uso 2: Embeddings con Neo4j

**Objetivo:** Búsqueda semántica en grafos

```cypher
// Crear índice de vectores (requiere GDS)
CALL gds.graph.project(
  'knowledge-graph',
  'Concepto',
  'RELACIONADO_CON'
)

// Generar embeddings con Ollama (via API)
// Luego almacenar en Neo4j con propiedad 'embedding'
```

**Usar con Copilot:**
```
@workspace "Genera embeddings para todos los conceptos 
en Neo4j usando Ollama, luego búscame conceptos 
similares a 'inteligencia artificial'"
```

### Caso de Uso 3: Memoria Persistente

**Objetivo:** Que Copilot recuerde contexto entre sesiones

```
@workspace "Guarda en neo4j-memory que estoy trabajando 
en el proyecto Melquisedec, enfocado en grafos de conocimiento 
con Neo4j y embeddings con Ollama"
```

Luego en otra sesión:
```
@workspace "¿En qué proyecto estaba trabajando?"
```

---

## 🔧 Troubleshooting {#troubleshooting}

### Problema 1: Neo4j no se conecta

**Síntoma:**
```
❌ Error: Could not connect to Neo4j
```

**Solución:**
```powershell
# 1. Verificar que Neo4j está corriendo
docker ps | Select-String "melquisedec-neo4j"

# 2. Ver logs
docker logs melquisedec-neo4j

# 3. Verificar puerto
Test-NetConnection -ComputerName localhost -Port 7687

# 4. Reiniciar Neo4j
docker-compose restart neo4j
```

### Problema 2: MCP requiere secretos

**Síntoma:**
```
⚠️  Requiere secretos
```

**Solución:**
```powershell
# Listar secretos faltantes
docker mcp server show <nombre>

# Configurar secreto
docker mcp secret set <server> <KEY> <value>

# Ejemplo: Brave
docker mcp secret set brave BRAVE_API_KEY tu_api_key_aqui
```

### Problema 3: MCPs no aparecen en Copilot

**Síntoma:**
Los MCPs están habilitados pero Copilot no los ve

**Solución:**
```powershell
# 1. Verificar conexión del cliente
docker mcp client ls --global

# 2. Reconectar VS Code
docker mcp client connect vscode

# 3. Reiniciar VS Code
# 4. Verificar que MCP_DOCKER aparece en la lista
```

### Problema 4: Timeout en pruebas

**Síntoma:**
```
ERROR: Timeout
```

**Solución:**
```powershell
# Aumentar timeout
python scripts/test_docker_mcp_toolkit.py --timeout 60

# O verificar conectividad de red
docker mcp gateway run --verify-signatures
```

---

## 📚 Comandos Útiles

### Docker MCP Toolkit

```powershell
# Listar servidores
docker mcp server ls

# Ver detalles de un servidor
docker mcp server show neo4j-cypher

# Habilitar servidor
docker mcp server enable <nombre>

# Deshabilitar servidor
docker mcp server disable <nombre>

# Listar secretos
docker mcp secret ls

# Ver configuración
docker mcp config show

# Actualizar catálogo
docker mcp catalog update
```

### Neo4j

```powershell
# Acceder a cypher-shell
docker exec -it melquisedec-neo4j cypher-shell -u neo4j -p password123

# Crear base de datos memory
docker exec melquisedec-neo4j cypher-shell -u neo4j -p password123 -d system "CREATE DATABASE memory IF NOT EXISTS"

# Ver estadísticas
docker exec melquisedec-neo4j cypher-shell -u neo4j -p password123 "CALL dbms.components() YIELD name, versions"
```

### Docker Compose

```powershell
# Iniciar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f neo4j

# Reiniciar servicio
docker-compose restart neo4j

# Detener todo
docker-compose down

# Limpiar volúmenes (¡cuidado!)
docker-compose down -v
```

---

## 🎓 Mejores Prácticas

1. **Configuración Incremental**
   - Habilita MCPs uno por uno
   - Prueba cada MCP antes de continuar
   - Documenta configuraciones específicas

2. **Gestión de Secretos**
   - NUNCA commites secretos en git
   - Usa Docker secrets en lugar de env vars
   - Rota API keys regularmente

3. **Monitoreo**
   - Ejecuta test_docker_mcp_toolkit.py semanalmente
   - Revisa logs de Neo4j para detectar problemas
   - Monitorea uso de memoria de Ollama

4. **Backups**
   - Exporta datos de Neo4j regularmente
   - Guarda configuración de MCPs
   - Documenta cambios en arquitectura

---

## 🚀 Próximos Pasos

1. ✅ Ejecutar `setup_neo4j_mcp.ps1`
2. ✅ Probar con `test_docker_mcp_toolkit.py`
3. ✅ Verificar en Neo4j Browser (http://localhost:7474)
4. ✅ Crear primer grafo de conocimiento
5. ✅ Usar Copilot para consultar grafos
6. 🔄 Optimizar configuración según uso
7. 🔄 Agregar más MCPs según necesidad

---

**Última actualización:** 2026-01-07  
**Autor:** GitHub Copilot + Aleia Melquisedec Team
