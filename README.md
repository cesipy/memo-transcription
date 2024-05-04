# Transcription

This project processes audio files and transcribes them into text. It supports processing of a single file or all files in a directory.

## Project Structure


- `src/`: Contains the source code for the project.
  - `main.py`: The main script that runs the audio processing.
  - `preprocess.py`: Contains functions for preprocessing audio files.
  - `logger.py`: Contains the Logger class for logging information and errors.
- `res/`: Contains the audio files to be processed and the output text files.
  - `converted/`: Contains the converted audio files.
  - `output/`: Contains the output text files from the audio processing.
- `logs/`: Contains log files.

## How to Run

1. Install the required packages listed in `requirements.txt` using:
    ```bash
    pip install -r requriements.txt
    ```
2. Run the `main.py` script with the appropriate arguments.
    ```bash
    python src/main.py 

### Arguments


- `--path`: The path to the directory containing the audio files to process. Default is "res".
- `--model`: The model to use for transcription. Options are "base", "medium", "large". Default is "large".
- `--file`: The path to a single audio file to process.

## Example

```sh
python src/main.py  --model large --file res/audio.wav
``` 
