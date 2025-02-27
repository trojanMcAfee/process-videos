from openai import OpenAI
import os
from dotenv import load_dotenv
import argparse
import sys

# Load environment variables
load_dotenv()

def transcribe_audio(audio_file_path):
    """
    Transcribe an audio file and save the transcript in the one-video directory.
    
    Args:
        audio_file_path (str): Path to the audio file to transcribe
    """
    # Initialize OpenAI client
    client = OpenAI()  # This will automatically use OPENAI_API_KEY from environment
    
    # Get the current directory where the script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    one_video_dir = os.path.join(base_dir, "one-video")
    
    # Create one-video directory if it doesn't exist
    os.makedirs(one_video_dir, exist_ok=True)
    
    # Check if file exists
    if not os.path.exists(audio_file_path):
        print(f"Error: File not found: {audio_file_path}")
        sys.exit(1)
        
    # Check if file is an audio file
    if not audio_file_path.lower().endswith('.mp3'):
        print("Error: File must be an MP3 file")
        sys.exit(1)
    
    print(f"Processing {os.path.basename(audio_file_path)}...")
    
    # Open and transcribe the audio file
    with open(audio_file_path, "rb") as audio_file:
        try:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="json"
            )
        except Exception as e:
            print(f"Error during transcription: {str(e)}")
            sys.exit(1)

    # Create output filename based on input filename
    output_filename = f"{os.path.splitext(os.path.basename(audio_file_path))[0]}_transcript.md"
    output_path = os.path.join(one_video_dir, output_filename)

    # Save the transcription to a file
    with open(output_path, "w") as f:
        f.write(f"# {os.path.splitext(os.path.basename(audio_file_path))[0]} - Transcript\n\n")
        f.write(transcription.text)

    print(f"Transcription saved to {output_path}")
    print("\nTranscription completed!")

def main():
    parser = argparse.ArgumentParser(
        description='Transcribe an audio file using OpenAI Whisper API\n\n'
                  'This script can be called in two ways:\n'
                  '  python one_video_transcribe.py path/to/your/audio.mp3\n'
                  '  python transcribe path/to/your/audio.mp3',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('audio_path', help='Path to the audio file to transcribe')
    
    args = parser.parse_args()
    transcribe_audio(args.audio_path)

if __name__ == "__main__":
    main() 