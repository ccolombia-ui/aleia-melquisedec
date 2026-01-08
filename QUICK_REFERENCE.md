# Quick Reference - DAATH-ZEN MELQUISEDEC

Comandos rápidos y atajos para trabajar con el monorepo.

---

## 🚀 Setup Inicial

```powershell
# Clonar y configurar
git clone https://github.com/tu-org/aleia-melquisedec.git
cd aleia-melquisedec
cp .env.example .env
code .env  # Editar credenciales

# Levantar infraestructura
cd infrastructure/docker
docker-compose up -d

# Configurar MCP servers
cd ../../tools/setup
.\setup_neo4j_simple.ps1

# Validar
cd ../testing
python test_mcp_toolkit.py --verbose
```

---

## 📁 Crear Nueva Investigación

```powershell
# Forma rápida
python packages/daath-toolkit/generators/new_research.py mi-investigacion

# Con opciones
python packages/daath-toolkit/generators/new_research.py knowledge-graphs \
  --purpose "Analizar estructuras de grafos de conocimiento" \
  --initiated-by HYPATIA
```

---

## ✅ Validar Estructura

```powershell
# Validar una investigación
python packages/daath-toolkit/validators/validate_research.py apps/01-mi-app

# Validar todas
Get-ChildItem apps -Directory | Where-Object { $_.Name -match '^\d' } | ForEach-Object {
    python packages/daath-toolkit/validators/validate_research.py $_.FullName
}
```

---

## 🧪 Testing

```powershell
# Test de MCPs
python tools/testing/test_mcp_toolkit.py
python tools/testing/test_mcp_toolkit.py --verbose  # Con detalles

# Test de configuración .mcp.json (para Claude Desktop)
python tools/testing/test_mcps.py

# Validar investigación específica
python packages/daath-toolkit/validators/validate_research.py apps/01-*
```

---

## 🐳 Docker

```powershell
# Levantar todo
cd infrastructure/docker
docker-compose up -d

# Solo Neo4j
docker-compose up -d neo4j

# Solo Ollama
docker-compose up -d ollama

# Ver logs
docker-compose logs -f neo4j
docker-compose logs -f ollama

# Bajar servicios
docker-compose down

# Limpiar volúmenes (⚠️ borra datos)
docker-compose down -v
```

---

## 🗄️ Neo4j

```powershell
# Abrir Neo4j Browser
start http://localhost:7474
# Usuario: neo4j, Password: password123

# Crear base de datos 'memory'
docker exec -it melquisedec-neo4j cypher-shell -u neo4j -p password123 "CREATE DATABASE memory IF NOT EXISTS"

# Listar bases de datos
docker exec -it melquisedec-neo4j cypher-shell -u neo4j -p password123 "SHOW DATABASES"

# Backup (básico)
docker exec melquisedec-neo4j neo4j-admin database dump neo4j --to=/var/lib/neo4j/backups/neo4j.dump
```

---

## 🤖 MCP Servers

```powershell
# Listar servers
docker mcp server ls

# Configurar server
docker mcp config set <server-name> <key> <value>
docker mcp secret set <server-name> <key> <value>

# Ejemplos
docker mcp config set neo4j-cypher NEO4J_URI bolt://localhost:7687
docker mcp secret set brave BRAVE_API_KEY tu-api-key

# Ver configuración
docker mcp config get <server-name>

# Reiniciar server
docker mcp server restart <server-name>
```

---

## 📝 Git Workflow

```powershell
# Crear rama para nueva feature
git checkout -b feature/nueva-funcionalidad

# Commits siguiendo convención
git add .
git commit -m "feat(core-mcp): agregar validación de configuración"
git commit -m "fix(tools): corregir encoding en setup script"
git commit -m "docs(guides): actualizar guía de MCP Toolkit"

# Push
git push origin feature/nueva-funcionalidad

# Pull request
gh pr create --title "feat: nueva funcionalidad" --body "Descripción..."
```

---

## 📚 Documentación

```powershell
# Ver arquitectura
code ARQUITECTURA_MONOREPO.md

# Ver resumen de reorganización
code REORGANIZACION_COMPLETA.md

# Ver estructura visual
code ESTRUCTURA_VISUAL.md

# Ver guía de contribución
code CONTRIBUTING.md

# Ver manifiesto
code docs/manifiesto/bereshit-v3.0.0.md
```

---

## 🔍 Búsqueda Rápida

```powershell
# Buscar en código
grep -r "search_term" packages/

# Buscar archivos
fd "pattern" packages/

# Buscar en investigaciones
grep -r "keyword" apps/*/

# Listar archivos PROPOSITO
Get-ChildItem -Path apps -Filter "PROPOSITO.md" -Recurse
```

---

## 🧹 Limpieza

```powershell
# Limpiar Python cache
Get-ChildItem -Path . -Include __pycache__ -Recurse -Force | Remove-Item -Recurse -Force

# Limpiar logs
Remove-Item -Path "*.log" -Force

# Eliminar app de prueba
Remove-Item -Path "apps/01-test-reorganizacion" -Recurse -Force
```

---

## 📊 Métricas

```powershell
# Contar investigaciones activas
(Get-ChildItem apps -Directory | Where-Object { $_.Name -match '^\d' }).Count

# Contar archivos por investigación
Get-ChildItem apps/01-* -Recurse -File | Measure-Object | Select-Object Count

# Ver tamaño de investigación
Get-ChildItem apps/01-* -Recurse | Measure-Object -Property Length -Sum

# Listar carpetas creadas (no vacías)
Get-ChildItem apps/01-*/* -Directory | Where-Object {
    (Get-ChildItem $_.FullName -File).Count -gt 0
}
```

---

## 🎯 GitHub Copilot - Prompts Útiles

```
# Crear grafo de conocimiento
@workspace Usando neo4j-cypher MCP, crea un grafo de conocimiento para [tema]

# Buscar papers
@workspace Con arxiv MCP, busca papers sobre [tema] publicados después de 2020

# Investigación profunda
@workspace Usando perplexity-ask, investiga [pregunta] y resume en 3 puntos clave

# Generar embeddings
@workspace Con ollama, genera embeddings para los conceptos en apps/01-*/2-atomic/

# Validar estructura
@workspace Valida que apps/01-* siga los principios DAATH-ZEN

# Crear visualización
@workspace Crea una visualización del grafo de conocimiento en apps/01-*/4-dataset/
```

---

## 🛠️ Troubleshooting

```powershell
# Neo4j no inicia
docker-compose logs neo4j
docker-compose restart neo4j

# MCP server no responde
docker mcp server ls
docker mcp server restart <server-name>

# Python module not found
cd packages/core-mcp
pip install -r requirements.txt

# Puerto ocupado
netstat -ano | findstr :7474
netstat -ano | findstr :7687

# Limpiar y reiniciar todo
docker-compose down -v
docker-compose up -d
.\tools\setup\setup_neo4j_simple.ps1
```

---

## 🔗 Enlaces Rápidos

- 📖 Docs: `docs/`
- 🏗️ Arquitectura: `ARQUITECTURA_MONOREPO.md`
- ✅ ADRs: `docs/architecture/`
- 🎯 Manifiesto: `docs/manifiesto/bereshit-v3.0.0.md`
- 🤝 Contribuir: `CONTRIBUTING.md`

---

## 💡 Tips

1. **Usar el generador**: No crear apps manualmente
2. **Validar siempre**: Antes de commit, validar estructura
3. **Commits atómicos**: Un cambio = un commit
4. **Documentar decisiones**: Usar ADRs para cambios importantes
5. **Tests primero**: Validar antes de pushear

---

**Mantén esta referencia a mano para trabajar más rápido** ⚡
