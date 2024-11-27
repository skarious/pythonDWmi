# Media Processing API

Esta API permite procesar contenido multimedia y descargarlo en la mejor calidad disponible.

## Características

- Descarga y procesa contenido multimedia de manera eficiente.
- Combina automáticamente el mejor video y audio disponibles.
- Accesible mediante solicitudes POST.

## Requisitos

- Python 3.7 o superior.
- `yt-dlp`, `Flask`, y `gunicorn` como dependencias.

## Despliegue en Render

Sigue estos pasos para desplegar la API en Render:

1. **Preparar el proyecto**:
   - Clona este repositorio:
     ```bash
     git clone https://github.com/tu_usuario/tu_repositorio.git
     cd tu_repositorio
     ```

   - Asegúrate de que los archivos requeridos estén presentes:
     - `content_service.py`
     - `requirements.txt`
     - `start.sh`

2. **Crear un servicio web en Render**:
   - Ve a [Render](https://render.com/) y crea una cuenta.
   - Crea un nuevo **Web Service** y conecta este repositorio.
   - Configura los comandos de inicio:
     ```bash
     ./start.sh
     ```

3. **Probar la API**:
   Una vez desplegada, Render proporcionará una URL pública (por ejemplo, `https://content-service.onrender.com`).

   Usa herramientas como `curl` para interactuar con la API:

   ```bash
   curl -X POST https://content-service.onrender.com/process \
   -H "Content-Type: application/json" \
   -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
