from flask import Flask, request, jsonify, send_file
import os
import subprocess
from moviepy.editor import VideoFileClip

app = Flask(__name__)

@app.route('/convertir', methods=['POST'])
def convertir_video():
  
    if 'archivo' not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    archivo = request.files['archivo'] 
    nombre = request.form.get('nombre')

   
    input_path = "D:\\Python\\" + nombre + ".webm"
    archivo.save(input_path)

    output_path = "D:\\Python\\RULETAROYAL.mp4" 

    try:
        
        command = ["ffmpeg", "-i", input_path, "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", output_path]
        subprocess.run(command, check=True)

        os.remove(input_path)

        return send_file(output_path, as_attachment=True, download_name="RULETAROYAL.mp4") #DEVOLVER EL ARCHIVO CONVERTIDO

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
