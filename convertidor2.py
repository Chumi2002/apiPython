import subprocess
import sys
from moviepy.editor import VideoFileClip

def convertir_video(input_path, output_path):
    command = ["ffmpeg", "-i", input_path, "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", output_path]
    subprocess.run(command, check=True)
    print(f"Video convertido y guardado en: {output_path}")

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convertir_video(input_path, output_path)

    video_clip = VideoFileClip(output_path)
    print(f"Duración del video convertido: {video_clip.duration} segundos")
