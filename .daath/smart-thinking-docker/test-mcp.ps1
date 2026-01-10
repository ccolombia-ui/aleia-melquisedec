# Test simple de smart-thinking MCP server
# Diagnóstico completo del container Docker

Write-Host "`n=== 1. Estado del Container ===" -ForegroundColor Cyan
docker ps --filter name=smart-thinking --format "table {{.Names}}`t{{.Status}}`t{{.Image}}"

Write-Host "`n=== 2. Inspect Container ===" -ForegroundColor Cyan
docker inspect smart-thinking-mcp --format "{{json .State}}" | ConvertFrom-Json | Format-List

Write-Host "`n=== 3. Variables de Entorno ===" -ForegroundColor Cyan
docker exec smart-thinking-mcp env | Select-String "TELEMETRY|THINKING"

Write-Host "`n=== 4. Verificar ejecutable ===" -ForegroundColor Cyan
docker exec smart-thinking-mcp which smart-thinking-mcp

Write-Host "`n=== 5. Test manual stdio (5 segundos) ===" -ForegroundColor Cyan
Write-Host "Iniciando MCP server..." -ForegroundColor Yellow

$job = Start-Job -ScriptBlock {
    docker exec -i smart-thinking-mcp smart-thinking-mcp
}

Start-Sleep -Seconds 2

if ($job.State -eq "Running") {
    Write-Host "✅ Server inició correctamente" -ForegroundColor Green
    Stop-Job $job
    Remove-Job $job
} else {
    Write-Host "❌ Server falló al iniciar" -ForegroundColor Red
    Receive-Job $job
    Remove-Job $job
}

Write-Host "`n=== 6. Logs recientes (últimas 10 líneas) ===" -ForegroundColor Cyan
docker logs smart-thinking-mcp --tail 10

Write-Host "`n=== 7. Verificar volumen montado ===" -ForegroundColor Cyan
docker exec smart-thinking-mcp ls -la /data/sessions

Write-Host "`n=== 8. Test MCP initialize (método directo) ===" -ForegroundColor Cyan
Write-Host "Enviando mensaje initialize..." -ForegroundColor Yellow

$initMsg = '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0.0"}}}'

# Crear archivo temporal con el mensaje
$tempFile = New-TemporaryFile
$initMsg | Set-Content $tempFile.FullName -NoNewline

# Enviar al container y capturar respuesta
$response = Get-Content $tempFile.FullName | docker exec -i smart-thinking-mcp smart-thinking-mcp

Remove-Item $tempFile.FullName

if ($response) {
    Write-Host "✅ Respuesta recibida:" -ForegroundColor Green
    $response | ForEach-Object { Write-Host $_ -ForegroundColor White }
} else {
    Write-Host "❌ Sin respuesta del servidor" -ForegroundColor Red
}

Write-Host "`n=== Resumen ===" -ForegroundColor Cyan
Write-Host "Container: smart-thinking-mcp" -ForegroundColor Yellow
Write-Host "Comando: docker exec -i smart-thinking-mcp smart-thinking-mcp" -ForegroundColor Yellow
Write-Host "Config: User Settings (claudeCode.mcpServers) + .vscode/mcp.json" -ForegroundColor Yellow
