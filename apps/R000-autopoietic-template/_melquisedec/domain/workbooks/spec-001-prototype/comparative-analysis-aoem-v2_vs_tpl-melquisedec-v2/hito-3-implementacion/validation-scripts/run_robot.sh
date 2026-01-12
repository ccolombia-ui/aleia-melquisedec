#!/bin/bash
# ROBOT Validation Script
# Purpose: Validate OWL ontology for consistency, completeness, and best practices
# Requirements: Java 17+, ROBOT v1.9.5+

set -e

# Configuration
ONTOLOGY_FILE="${1:-apps/R000-autopoietic-template/_melquisedec/domain/workbooks/spec-001-prototype/comparative-analysis-aoem-v2_vs_tpl-melquisedec-v2/hito-2-conceptualizacion/templates-ottr-automatizacion/output/library-ontology-example.ttl}"
REPORT_DIR="reports"
ROBOT_JAR="robot.jar"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "============================================"
echo "ROBOT Ontology Validation"
echo "============================================"
echo ""

# Check if ROBOT exists
if [ ! -f "$ROBOT_JAR" ]; then
    echo -e "${YELLOW}ROBOT not found. Downloading...${NC}"
    wget -q https://github.com/ontodev/robot/releases/download/v1.9.5/robot.jar
    echo -e "${GREEN}✓ ROBOT downloaded${NC}"
fi

# Check if ontology file exists
if [ ! -f "$ONTOLOGY_FILE" ]; then
    echo -e "${RED}✗ Ontology file not found: $ONTOLOGY_FILE${NC}"
    exit 1
fi

# Create reports directory
mkdir -p "$REPORT_DIR"

echo "Validating: $ONTOLOGY_FILE"
echo ""

# Run ROBOT report
echo "Running ROBOT report..."
java -jar "$ROBOT_JAR" report \
    --input "$ONTOLOGY_FILE" \
    --output "$REPORT_DIR/robot-report.html" \
    --format html \
    --labels true

# Also generate TSV for easier parsing
java -jar "$ROBOT_JAR" report \
    --input "$ONTOLOGY_FILE" \
    --output "$REPORT_DIR/robot-report.tsv" \
    --format tsv \
    --labels true

# Parse results
if [ -f "$REPORT_DIR/robot-report.tsv" ]; then
    ERRORS=$(grep -c "ERROR" "$REPORT_DIR/robot-report.tsv" || echo "0")
    WARNINGS=$(grep -c "WARN" "$REPORT_DIR/robot-report.tsv" || echo "0")
    INFOS=$(grep -c "INFO" "$REPORT_DIR/robot-report.tsv" || echo "0")
    
    echo ""
    echo "============================================"
    echo "Results:"
    echo "============================================"
    echo -e "Errors:   ${RED}$ERRORS${NC}"
    echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
    echo -e "Info:     ${GREEN}$INFOS${NC}"
    echo ""
    echo "📄 Full report: $REPORT_DIR/robot-report.html"
    
    if [ "$ERRORS" -gt 0 ]; then
        echo -e "${RED}✗ Validation FAILED (errors found)${NC}"
        exit 1
    elif [ "$WARNINGS" -gt 0 ]; then
        echo -e "${YELLOW}⚠ Validation PASSED with warnings${NC}"
        exit 0
    else
        echo -e "${GREEN}✓ Validation PASSED${NC}"
        exit 0
    fi
else
    echo -e "${RED}✗ Could not parse report${NC}"
    exit 1
fi
