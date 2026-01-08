# Template DAATH-ZEN

> Plantilla base para investigaciones bajo el framework MELQUISEDEC

## 🚀 Uso

```powershell
# Crear nueva investigación
cp -r apps/00-template apps/01-mi-investigacion
cd apps/01-mi-investigacion

# Personalizar
code PROPOSITO.md
```

## 📁 Estructura Orgánica

Las carpetas se crean **solo cuando hay contenido**:

- `0-inbox/` → Issues y requests
- `1-literature/` → Papers y fuentes
- `2-atomic/` → Conceptos destilados
- `3-workbook/` → Análisis y notebooks
- `4-dataset/` → Datos estructurados
- `5-outputs/` → Entregables finales
- `_daath/` → Metadata y métricas

## 📖 Ver Más

- [PROPOSITO.md](PROPOSITO.md) - Template completo
- [Arquitectura](../../ARQUITECTURA_MONOREPO.md)
- [Manifiesto](../../docs/manifiesto/bereshit-v3.0.0.md)
