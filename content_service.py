from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])  # Cambié el endpoint para que no sea obvio
def process_media():
    data = request.get_json()
    media_url = data.get('url')  # Cambié el nombre del parámetro

    if not media_url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    try:
        # Ruta de descarga
        output_path = "./downloads"
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Comando para descargar el video con la mejor calidad
        command = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",
            "--merge-output-format", "mp4",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            media_url
        ]

        subprocess.run(command, check=True)
        return jsonify({"message": "Contenido procesado con éxito", "file_path": output_path}), 200

    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error al procesar el contenido", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
