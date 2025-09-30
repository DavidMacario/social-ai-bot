# Social AI Bot

MVP de herramienta de **automatización de publicaciones en redes sociales** y análisis de tendencias usando Python y técnicas de IA.

## Objetivo
Este proyecto permite:
- Detectar tendencias en X/Twitter.
- Generar borradores de publicaciones automáticamente mediante plantillas.
- Encolar posts en una base de datos para revisión posterior.
- Validar ideas de contenido de forma rápida y eficiente.

## Tecnologías usadas
- **Python 3.11+**
- **snscrape**: scraping de tweets
- **Jinja2**: plantillas de texto para generación de posts
- **SQLite**: base de datos ligera para la cola de posts
- **dotenv**: gestión de variables de entorno

## Estructura del proyecto
social-ai-bot/
├─ scripts/ # scripts Python
├─ db/ # base de datos SQLite
├─ sample_templates/ # plantillas de posts
├─ docs/ # documentación y roadmap
├─ requirements.txt
└─ README.md
