#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Creates a new research workbook from template

.DESCRIPTION
    This script creates a new workbook by cloning either the academic-research-template
    or imrad-template, populating metadata with current date and specified values.

.PARAMETER Type
    Template type: 'academic-research' or 'imrad'

.PARAMETER Topic
    Research topic name (e.g., "Domain-Driven Design")

.PARAMETER Agent
    Agent name (default: HYPATIA for academic-research, SALOMON for imrad)

.PARAMETER SpecIssue
    Spec issue reference (default: spec-000)

.EXAMPLE
    .\create-workbook.ps1 -Type academic-research -Topic "Domain-Driven Design"

.EXAMPLE
    .\create-workbook.ps1 -Type imrad -Topic "Daath-Zen Framework" -Agent SALOMON
#>

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('academic-research', 'imrad')]
    [string]$Type,

    [Parameter(Mandatory=$true)]
    [string]$Topic,

    [Parameter(Mandatory=$false)]
    [string]$Agent,

    [Parameter(Mandatory=$false)]
    [string]$SpecIssue = "spec-000"
)

# Configuration
$TemplatesDir = "00-define/0-define-daath-zen-framework/templates"
$WorkbooksDir = "00-define/0-define-daath-zen-framework/workbooks"
$IsoDate = Get-Date -Format "yyyy-MM-dd"

# Set default agent based on type
if (-not $Agent) {
    $Agent = if ($Type -eq 'academic-research') { 'HYPATIA' } else { 'SALOMON' }
}

# Create slug from topic (lowercase, hyphenated)
$TopicSlug = $Topic.ToLower() -replace '\s+', '-' -replace '[^a-z0-9\-]', ''

# Template paths
$TemplatePath = Join-Path $TemplatesDir "$Type-template"
$DestinationPath = Join-Path $WorkbooksDir "wb-$TopicSlug"

# Validation
if (-not (Test-Path $TemplatePath)) {
    Write-Error "Template not found: $TemplatePath"
    exit 1
}

if (Test-Path $DestinationPath) {
    Write-Error "Workbook already exists: $DestinationPath"
    Write-Host "Use a different topic name or delete existing workbook first."
    exit 1
}

Write-Host "Creating workbook: $DestinationPath" -ForegroundColor Cyan
Write-Host "  Type: $Type" -ForegroundColor Gray
Write-Host "  Topic: $Topic" -ForegroundColor Gray
Write-Host "  Agent: $Agent" -ForegroundColor Gray
Write-Host "  Date: $IsoDate" -ForegroundColor Gray
Write-Host ""

# Copy template
try {
    Copy-Item -Path $TemplatePath -Destination $DestinationPath -Recurse -Force
    Write-Host "✓ Template copied" -ForegroundColor Green
} catch {
    Write-Error "Failed to copy template: $_"
    exit 1
}

# Replace placeholders in all markdown files
$MarkdownFiles = Get-ChildItem -Path $DestinationPath -Filter "*.md" -Recurse

foreach ($File in $MarkdownFiles) {
    Write-Host "  Processing: $($File.Name)" -ForegroundColor Gray

    $Content = Get-Content -Path $File.FullName -Raw

    # Replace placeholders
    $Content = $Content -replace '\{\{TOPIC_NAME\}\}', $Topic
    $Content = $Content -replace '\{\{TOPIC_SLUG\}\}', $TopicSlug
    $Content = $Content -replace '\{\{AGENT_NAME\}\}', $Agent
    $Content = $Content -replace '\{\{ISO_DATE\}\}', $IsoDate
    $Content = $Content -replace '\{\{SPEC_ISSUE\}\}', $SpecIssue

    # Default values for optional fields
    $Content = $Content -replace '\{\{PRIMARY_SUBJECT\}\}', "Research"
    $Content = $Content -replace '\{\{SECONDARY_SUBJECT\}\}', "$Topic"
    $Content = $Content -replace '\{\{ADDITIONAL_CONTRIBUTORS\}\}', ""

    # Save updated content
    Set-Content -Path $File.FullName -Value $Content -NoNewline
}

Write-Host "✓ Metadata populated in all files" -ForegroundColor Green
Write-Host ""

# Summary
Write-Host "Workbook created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Location: $DestinationPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Review README.md and update metadata as needed"
Write-Host "  2. Follow the workflow documented in README.md"

if ($Type -eq 'academic-research') {
    Write-Host "  3. Start with literature collection (1-literature/)"
    Write-Host "  4. Proceed to analysis, atomics, and synthesis"
} else {
    Write-Host "  3. Start with Introduction (01-introduction.md)"
    Write-Host "  4. Fill in all 7 IMRAD sections sequentially"
}

Write-Host "  5. Validate with: python tools/validation/validate-$Type.py $DestinationPath"
Write-Host ""

Write-Host "Happy researching! 📚✨" -ForegroundColor Magenta
