# 📧 Automatización de Reportes de Cursos

Script en Python que automatiza la recopilación de datos de alumnos desde Gmail y genera un archivo Excel listo para enviar a matriz y generar diplomas.

---

## 🎯 Problema que resuelve

En cursos de capacitación, los alumnos envían sus datos por correo para obtener su diploma:

```
Nombre: Juan Pérez
Profesión: Ingeniero Civil
Empresa: Constructora ABC
```

El proceso manual implica revisar cada correo, copiar los datos y llenar un Excel uno por uno. Con grupos grandes, esto consume mucho tiempo y genera errores de captura.

**Este script hace todo eso automáticamente.**

---

## ⚙️ Cómo funciona

```
Gmail
 ↓
Python lee los correos automáticamente
 ↓
Extrae los datos del alumno (aunque vengan desordenados)
 ↓
Estructura la información en JSON
 ↓
Guarda todo en un archivo Excel
 ↓
Archivo listo para enviar a matriz
```

---

## 📁 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `leer_gmail.py` | Conexión y autenticación con Gmail API. Lee los correos de la bandeja. |
| `leer_correos.py` | Filtra los correos relevantes del curso. |
| `extraer.py` | Extrae los datos del alumno del cuerpo del correo. |
| `extraer_001.py` | Versión mejorada del extractor, maneja formatos inconsistentes. |
| `procesar_correos.py` | Orquesta todo el flujo: lee, extrae y guarda en Excel. |
| `alumnos.csv` | Ejemplo del resultado: datos estructurados de alumnos. |
| `Curso Basico 2026.xlsx` | Plantilla de reporte final para enviar a matriz. |

---

## 🛠️ Tecnologías usadas

- Python 3
- Gmail API (Google Cloud)
- `google-api-python-client`
- `google-auth` / `google-auth-oauthlib`
- `openpyxl` (manejo de Excel)

---

## 🚀 Estado del proyecto

- [x] Proyecto Google Cloud configurado
- [x] Gmail API habilitada
- [x] Autenticación OAuth configurada
- [x] Script base de lectura de correos creado
- [x] Extracción de datos implementada
- [ ] Pruebas con correos reales completadas
- [ ] Generación automática del Excel final

---

## 💡 Contexto

Proyecto desarrollado para automatizar el proceso de registro de alumnos en cursos de capacitación técnica (Neodata Precios Unitarios). El instructor imparte el curso, los alumnos envían sus datos por correo, y el sistema genera el reporte para emisión de diplomas sin intervención manual.

---

## ⚠️ Nota de seguridad

El archivo `credenciales.json` (clave de acceso a Gmail API) **no está incluido** en este repositorio por razones de seguridad. Para usar este proyecto necesitas configurar tu propio proyecto en Google Cloud y descargar tus propias credenciales.
