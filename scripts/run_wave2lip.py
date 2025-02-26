import os
import subprocess

# Paths
image_path = "input/input_image.jpg"
mp3_audio_path = "input/input_audio.mp3"
wav_audio_path = "input/input_audio.wav"
checkpoint_path = "checkpoints/wav2lip.pth"
output_video_path = "output/output_video.mp4"

# Run TTS
print(" Generating TTS audio...")
subprocess.run("python scripts/tts_generator.py", shell=True)

# Convert MP3 to WAV
print(" Converting MP3 to WAV...")
subprocess.run("python scripts/audio_converter.py", shell=True)

# Run Wav2Lip
print(" Running Wav2Lip model...")
command = f"python scripts/inference.py --checkpoint_path {checkpoint_path} --face {image_path} --audio {wav_audio_path} --outfile {output_video_path}"
subprocess.run(command, shell=True)

print(f"Lip-synced video saved at: {output_video_path}")
