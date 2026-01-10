# Script para configurar smart-thinking en Claude Code extension
# Autor: DAATH-ZEN MELQUISEDEC
# Fecha: 2026-01-09

$settingsPath = "$env:APPDATA\Code\User\settings.json"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Configurador MCP para Claude Code" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# 1. Verificar que existe settings.json
if (-not (Test-Path $settingsPath)) {
    Write-Host "❌ No se encontró settings.json en: $settingsPath" -ForegroundColor Red
    exit 1
}

# 2. Leer settings.json
try {
    $settings = Get-Content $settingsPath -Raw | ConvertFrom-Json
} catch {
    Write-Host "❌ Error al parsear settings.json: $_" -ForegroundColor Red
    exit 1
}

# 3. Verificar que existe claudeCode.mcpServers
if (-not $settings.PSObject.Properties['claudeCode.mcpServers']) {
    Write-Host "❌ No se encontró 'claudeCode.mcpServers' en settings.json" -ForegroundColor Red
    Write-Host "   Esta extensión no está configurada correctamente." -ForegroundColor Yellow
    exit 1
}

$mcpServers = $settings.'claudeCode.mcpServers'

# 4. Configuración de smart-thinking
$smartThinkingConfig = @{
    command = "npx"
    args = @("-y", "smart-thinking-mcp")
    env = @{
        DISABLE_TELEMETRY = "true"
        TELEMETRY_DISABLED = "1"
        DO_NOT_TRACK = "1"
        SMART_THINKING_DATA_DIR = "C:/proyectos/aleia-melquisedec/.daath/smart-thinking-sessions"
    }
}

# 5. Configuración de sequential-thinking
$sequentialThinkingConfig = @{
    command = "npx"
    args = @("-y", "@modelcontextprotocol/server-sequential-thinking")
    env = @{
        DISABLE_TELEMETRY = "true"
        TELEMETRY_DISABLED = "1"
        DO_NOT_TRACK = "1"
    }
}

# 6. Configuración de maxential-thinking
$maxentialThinkingConfig = @{
    command = "npx"
    args = @("-y", "@bam-devcrew/maxential-thinking-mcp@2.0.1")
    env = @{
        DISABLE_TELEMETRY = "true"
        TELEMETRY_DISABLED = "1"
        DO_NOT_TRACK = "1"
    }
}

# 7. Agregar o actualizar servidores
$mcpServers | Add-Member -Name "smart-thinking" -Value $smartThinkingConfig -MemberType NoteProperty -Force
$mcpServers | Add-Member -Name "sequential-thinking" -Value $sequentialThinkingConfig -MemberType NoteProperty -Force
$mcpServers | Add-Member -Name "maxential-thinking" -Value $maxentialThinkingConfig -MemberType NoteProperty -Force

# 8. Guardar settings.json con formato bonito
$settings.'claudeCode.mcpServers' = $mcpServers
$settingsJson = $settings | ConvertTo-Json -Depth 10

# Reemplazar formato feo de PowerShell por formato bonito
$settingsJson = $settingsJson -replace '\\u0026', '&' -replace '\\u003c', '<' -replace '\\u003e', '>'

Set-Content -Path $settingsPath -Value $settingsJson -Encoding UTF8

Write-Host "✅ smart-thinking agregado/actualizado" -ForegroundColor Green
Write-Host "✅ sequential-thinking agregado/actualizado" -ForegroundColor Green
Write-Host "✅ maxential-thinking agregado/actualizado" -ForegroundColor Green
Write-Host ""
Write-Host "Configuracion guardada en:" -ForegroundColor Cyan
Write-Host "   $settingsPath" -ForegroundColor White
Write-Host ""
Write-Host "REINICIA VS CODE para que los cambios tomen efecto." -ForegroundColor Yellow
Write-Host ""
