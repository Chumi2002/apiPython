import subprocess

def convertir_video(input_path, output_path):
    command = ["ffmpeg", "-i", input_path, "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", output_path]
    subprocess.run(command, check=True)
    print(f"Video convertido y guardado en: {output_path}")

input_path = "D:\\Python\\RULETAROYAL.webm"
output_path = "D:\\Python\\GIRO MILLONARIO2.mp4"
convertir_video(input_path, output_path)

from moviepy.editor import VideoFileClip
video_clip = VideoFileClip(output_path)
print(f"Duración del video convertido: {video_clip.duration} segundos")


