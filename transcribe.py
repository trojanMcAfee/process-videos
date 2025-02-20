from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI()

# Get the current directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths
videos_dir = os.path.join(base_dir, "videos")
transcripts_dir = os.path.join(base_dir, "transcripts")

# Create directories if they don't exist
os.makedirs(videos_dir, exist_ok=True)
os.makedirs(transcripts_dir, exist_ok=True)

# Get all audio files from videos directory
audio_files = [f for f in os.listdir(videos_dir) if f.endswith('.mp3') and f != 'constructor_part_0.mp3']

if not audio_files:
    print("No audio files found in the videos directory (excluding constructor_part_0.mp3)")
    exit()

# Process each audio file
for audio_file_name in audio_files:
    audio_file_path = os.path.join(videos_dir, audio_file_name)
    
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
    output_path = os.path.join(transcripts_dir, output_filename)

    # Save the transcription to a file
    with open(output_path, "w") as f:
        f.write(f"# {os.path.splitext(audio_file_name)[0]} - Transcript\n\n")
        f.write(transcription.text)

    print(f"Transcription saved to {output_path}")

print("\nAll transcriptions completed!")