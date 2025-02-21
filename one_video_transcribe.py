from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()  # This will automatically use OPENAI_API_KEY from environment

# Get the current directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths
one_video_dir = os.path.join(base_dir, "one-video")

# Create directory if it doesn't exist
os.makedirs(one_video_dir, exist_ok=True)

# Get the audio file from one-video directory
audio_files = [f for f in os.listdir(one_video_dir) if f.endswith('.mp3')]

if not audio_files:
    print("No audio files found in the one-video directory")
    exit()

if len(audio_files) > 1:
    print("Warning: Multiple audio files found. Processing only the first one.")

# Process the audio file
audio_file_name = audio_files[0]
audio_file_path = os.path.join(one_video_dir, audio_file_name)

print(f"Processing {audio_file_name}...")

# Open and transcribe the audio file
with open(audio_file_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="json"
    )

# Create output filename based on input filename
output_filename = f"{os.path.splitext(audio_file_name)[0]}_transcript.md"
output_path = os.path.join(one_video_dir, output_filename)

# Save the transcription to a file
with open(output_path, "w") as f:
    f.write(f"# {os.path.splitext(audio_file_name)[0]} - Transcript\n\n")
    f.write(transcription.text)

print(f"Transcription saved to {output_path}")
print("\nTranscription completed!") 