# Wav2Lip - Lip Sync Implementation

This project implements the **Wav2Lip** model for lip synchronization using **gTTS (Google Text-to-Speech)** for generating audio and **FFmpeg** for audio conversion. The model generates a lip-synced video using an input face image or video and an audio file.

## 📌 Features
- **Lip-syncing with Wav2Lip** using a face image or video.
- **TTS (Text-to-Speech)** with an Indian accent using gTTS.
- **Audio conversion (MP3 to WAV 16kHz)** using FFmpeg.
- **Automated pipeline** to generate lip-synced videos.

---

## 🛠️ Setup Instructions

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/wav2lip-lip-sync.git
cd wav2lip-lip-sync
```

### 2️⃣ **Install Dependencies**
Make sure you have **Python 3.7+** and **FFmpeg** installed.
```bash
pip install -r requirements.txt
```

If FFmpeg is not installed, install it manually:
```bash
sudo apt install ffmpeg  # Linux
brew install ffmpeg  # macOS
winget install FFmpeg  # Windows
```

### 3️⃣ **Download the Wav2Lip Model Checkpoints**
```bash
mkdir -p checkpoints && cd checkpoints
wget -O wav2lip.pth "https://www.adrianbulat.com/downloads/python-fan/wav2lip.pth"
cd ..
```

---

## 📂 Project Structure
```
📂 wav2lip-lip-sync
│── 📂 input                  # Input folder (image/video & audio)
│   ├── input_image.jpg       # Face image (or video)
│   ├── input_audio.mp3       # TTS-generated audio
│   ├── input_audio.wav       # Converted WAV (16kHz)
│
│── 📂 output                 # Output folder (final video)
│   ├── output_video.mp4      # Lip-synced video
│
│── 📂 checkpoints            # Wav2Lip model checkpoints
│   ├── wav2lip.pth           # Model file
│
│── 📂 scripts
│   ├── inference.py          # Main Wav2Lip script
│   ├── tts_generator.py      # gTTS-based TTS script
│   ├── audio_converter.py    # Converts MP3 to WAV (16kHz)
│   ├── run_wav2lip.py        # Master script to run everything
│
│── requirements.txt          # Dependencies
│── README.md                 # Instructions
```

---

## 🚀 How to Use

### 1️⃣ **Generate Speech from Text (TTS)**
Run the **TTS generator** to create an audio file from text.
```bash
python scripts/tts_generator.py --text "Hello, this is a test!" --output input/input_audio.mp3
```

### 2️⃣ **Convert Audio to WAV (16kHz)**
```bash
python scripts/audio_converter.py --input input/input_audio.mp3 --output input/input_audio.wav
```

### 3️⃣ **Run Wav2Lip for Lip-Syncing**
```bash
python scripts/inference.py --checkpoint_path checkpoints/wav2lip.pth \
    --face input/input_image.jpg --audio input/input_audio.wav \
    --outfile output/output_video.mp4
```

### 4️⃣ **Run the Full Pipeline in One Command**
```bash
python scripts/run_wav2lip.py
```

---

## 🛠️ Troubleshooting

### 1️⃣ **Model Not Found Error**
Make sure you have downloaded the model checkpoint and placed it in the `checkpoints/` folder.

### 2️⃣ **Audio Conversion Issues**
Check if `ffmpeg` is installed correctly.
```bash
ffmpeg -version
```

### 3️⃣ **Misaligned Lips in Output**
- Try **disabling smoothing** by modifying `inference.py`:
  ```python
  parser.add_argument('--nosmooth', action='store_true', help='Disable smoothing')
  ```
- Run with `--nosmooth`:
  ```bash
  python scripts/inference.py --checkpoint_path checkpoints/wav2lip.pth \
      --face input/input_image.jpg --audio input/input_audio.wav \
      --outfile output/output_video.mp4 --nosmooth
  ```

---






### 🔥 Now You Are Ready to Sync Lips Like a Pro! 🔥

