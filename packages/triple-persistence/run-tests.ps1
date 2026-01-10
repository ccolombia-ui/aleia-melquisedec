#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Run tests with coverage and generate reports for SonarQube

.DESCRIPTION
    This script runs pytest with coverage, generates reports in multiple formats,
    and optionally runs SonarQube scanner for code quality analysis.

.PARAMETER SonarQube
    Run SonarQube scanner after tests

.EXAMPLE
    .\run-tests.ps1

.EXAMPLE
    .\run-tests.ps1 -SonarQube
#>

param(
    [switch]$SonarQube
)

$ErrorActionPreference = "Stop"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Running Triple-Persistence Tests" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

# Change to package directory
$packageDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $packageDir

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -q -r requirements.txt
pip install -q -r requirements-dev.txt

# Run tests with coverage
Write-Host "Running tests with coverage..." -ForegroundColor Yellow
pytest tests/ `
    --cov=triple_persistence `
    --cov-report=term-missing `
    --cov-report=html `
    --cov-report=xml `
    --cov-branch `
    --junitxml=test-results.xml `
    -v

$testResult = $LASTEXITCODE

if ($testResult -eq 0) {
    Write-Host "All tests passed!" -ForegroundColor Green
} else {
    Write-Host "Tests failed!" -ForegroundColor Red
    exit $testResult
}

# Display coverage summary
Write-Host "Coverage Summary:" -ForegroundColor Yellow
Write-Host "   HTML Report: htmlcov/index.html" -ForegroundColor White
Write-Host "   XML Report: coverage.xml" -ForegroundColor White

# Open HTML coverage report
if (Test-Path "htmlcov/index.html") {
    Write-Host "`n🌐 Opening coverage report in browser..." -ForegroundColor Yellow
    Start-Process "htmlcov/index.html"
}

# Run SonarQube scanner if requested
if ($SonarQube) {
    Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Running SonarQube Analysis" -ForegroundColor Green

    # Check if sonar-scanner is available
    $sonarScanner = Get-Command sonar-scanner -ErrorAction SilentlyContinue

    if ($null -eq $sonarScanner) {
        Write-Host "SonarQube Scanner not found!" -ForegroundColor Red
        Write-Host "   Install from: https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/" -ForegroundColor Yellow
        Write-Host "   Or run: choco install sonarscanner" -ForegroundColor Yellow
    } else {
        # Run sonar scanner
        sonar-scanner `
            -Dsonar.host.url=$env:SONAR_HOST_URL `
            -Dsonar.login=$env:SONAR_TOKEN

        if ($LASTEXITCODE -eq 0) {
            Write-Host "SonarQube analysis complete!" -ForegroundColor Green
            Write-Host "   View results at: $env:SONAR_HOST_URL" -ForegroundColor White
        } else {
            Write-Host "SonarQube analysis completed with warnings" -ForegroundColor Yellow
        }
    }
}

Write-Host "\n========================================" -ForegroundColor Cyan
Write-Host "Test Run Complete" -ForegroundColor Green
Write-Host "========================================\n" -ForegroundColor Cyan

Write-Host "Quality Metrics:" -ForegroundColor Yellow

# Parse coverage percentage from coverage.xml
if (Test-Path "coverage.xml") {
    $coverageXml = [xml](Get-Content "coverage.xml")
    $coverage = $coverageXml.coverage.'line-rate'
    $coveragePercent = [math]::Round($coverage * 100, 2)
    Write-Host "   Coverage: $coveragePercent%" -ForegroundColor White
}

# Count tests
$testCount = (Select-String -Path "test-results.xml" -Pattern '<testcase' -AllMatches).Matches.Count
Write-Host "   Tests: $testCount" -ForegroundColor White

Write-Host "\nNext steps:" -ForegroundColor Cyan
Write-Host "   - Review coverage: htmlcov/index.html" -ForegroundColor White
Write-Host "   - Fix failing tests if any" -ForegroundColor White
Write-Host "   - Run with -SonarQube for code quality analysis" -ForegroundColor White
Write-Host ""
