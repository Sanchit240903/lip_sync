import subprocess

# Convert MP3 to WAV using ffmpeg
input_audio = "input/input_audio.mp3"
output_audio = "input/input_audio.wav"

command = f"ffmpeg -i {input_audio} -ar 16000 -ac 1 {output_audio}"
subprocess.run(command, shell=True)

print(f"✅ Converted audio saved at: {output_audio}")
