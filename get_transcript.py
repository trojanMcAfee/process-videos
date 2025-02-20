from openai import OpenAI
import os
from pathlib import Path
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Define input and output paths
    input_path = "/Users/dnyrm/Documents/defi/uniswap_v3/constructor_part_0.mp3"
    output_path = "/Users/dnyrm/Desktop/experiments/transcript.txt"
    
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input audio file not found at: {input_path}")
        
        # Open and transcribe the audio file
        with open(input_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the transcription to a file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcription)
            
        print(f"Transcription completed successfully. Output saved to: {output_path}")
        
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred during transcription: {str(e)}")

if __name__ == "__main__":
    main()
