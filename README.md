# Audio Transcription CLI

A command-line tool that uses OpenAI's Whisper API to transcribe audio files to markdown format.

## Setup

1. Clone this repository and navigate to its directory
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
5. Make the transcribe script executable:
   ```bash
   chmod +x transcribe
   ```

## Usage

You can use this script in two ways:

### 1. Using the full script name:
```bash
python one_video_transcribe.py path/to/your/audio.mp3
```

### 2. Using the shorter alias:
```bash
./transcribe path/to/your/audio.mp3
```

## Input

- The script accepts MP3 audio files
- The audio file can be located anywhere on your system - just provide the correct path

## Output

- Transcripts are saved in the `one-video` directory (created automatically if it doesn't exist)
- Output files are in markdown format with the naming pattern: `{original_filename}_transcript.md`
- The transcript includes a title derived from the original filename

## Help

To see usage instructions and available options:
```bash
python one_video_transcribe.py --help
```

## Directory Structure

```
.
├── .env                    # Environment variables (API key)
├── README.md               # This file
├── one-video/              # Output directory for transcripts
├── one_video_transcribe.py # Script for single video transcription
├── requirements.txt        # Project dependencies
├── transcribe              # Executable script (shorthand)
└── transcribe.py           # Original script for multiple videos
```

## Error Handling

The script includes error checking for:
- Missing audio files
- Unsupported file formats
- API authentication issues
- Transcription errors

Error messages will be displayed in the terminal if any issues occur.

## Requirements

- Python 3.x
- OpenAI API key
- Internet connection (for API access)
- MP3 audio files for transcription

## Dependencies

- openai>=1.0.0
- python-dotenv>=0.19.0

## Notes

- Keep your API key secure and never commit it to version control
- The script creates a `one-video` directory if it doesn't exist
- All transcripts are saved as markdown files for easy reading and formatting
- `transcribe.py` is the original script that handles multiple videos, while `one_video_transcribe.py` is optimized for single video transcription