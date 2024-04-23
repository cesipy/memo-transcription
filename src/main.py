import whisper
from logger import Logger
import os
import preprocess
import time
import random 
import argparse


# globale variable fürs model
model = None
logger = Logger()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some audio files.')
    parser.add_argument('--path', type=str, default="res",
                        help='The path to the directory containing the audio files to process.')
    parser.add_argument('--model', type=str, default="large",
                        help='The model to use for transcription. Options are "base", "medium", "large". Default is "large".')
    parser.add_argument('--file', type=str,
                        help='The path to a single audio file to process.')
    
    return parser.parse_args()

def transcribe_audio(path_to_audio: str):
    # es gibt verschiedene modesl, 'base', 'medium', 'large'
    # base funktioniert soweit gut, für evt. bessere performance die anderen 
    global model
    if model == None:
        model = whisper.load_model("large")  
    result = model.transcribe(path_to_audio)

    return result

def write_to_file(text_body: str, filename: str):
    with open(f"{filename}.txt", "w") as file:
        file.write(text_body)


def format_text(text: str):
    min_words_in_row = 14
    max_words_in_row = 16
    counter = 0
    current_line_limit = random.randint(min_words_in_row, max_words_in_row)
    words = text.split()
    formatted_text = ""
    for word in words:
        counter += 1
        formatted_text += word + " "
        if counter >= current_line_limit:
            formatted_text = formatted_text.rstrip() + "\n"
            counter = 0
            current_line_limit = random.randint(min_words_in_row, max_words_in_row)
    return formatted_text.rstrip()


def process_audio_file(audio_path: str):
    try:
        result = transcribe_audio(audio_path)
        result_string = result["text"]

        formatted_text = format_text(result_string)

        output_filename = preprocess.generate_output_filename(audio_path, "res/converted")
        output_filename = output_filename.replace(".mp3", "")
        full_path_filename = f"res/output/{output_filename}"

        logger.log(f"output filename before writing: {full_path_filename}")

        write_to_file(formatted_text, full_path_filename)
    except Exception as e:
        logger.log(f"Error processing audio file {audio_path}: {str(e)}")


def process_single_file(file_path: str):
    if file_path.endswith("m4a"): 
        
        output_file_path = preprocess.convert_to_wav(file_path)
        logger.log(f"preprocessing complete! current path: {output_file_path}")

        start = time.time()
        process_audio_file(output_file_path)
        end = time.time()
        logger.log(f"transcription succeeded in {end-start}")



def process_all_files_in_dir(dir_name: str):
    """
    processes all files with a given extension in a given directory. 
    the directory is specified in `dir_name`. the file extension is specified using `file_extension`.
    note: `file_extension` should be in a valid extension, aswell leace out the ".". 
    example: "mp3" for .mp3 files.
    """
    for filename in os.listdir(dir_name):
        if filename.endswith("m4a"):
    
            full_filename = os.path.join(dir_name, filename)
            logger.log(f"filename to process: {filename} with full path: {full_filename}")
            output_file_path = preprocess.convert_to_wav(full_filename)
            logger.log(f"preprocessing complete! current path: {output_file_path}")

            start = time.time()
            process_audio_file(output_file_path)
            end = time.time()
            logger.log(f"transcription succeeded in {end-start}")
            



def main():
    args = parse_arguments()

    start_main = time.time()
    logger.log("\nnew processing job.")

    global model
    model = whisper.load_model(args.model)

    if args.file:
        process_single_file(args.file)
    
    else:
        process_all_files_in_dir(args.path)

    end_main = time.time()
    logger.log(f"----------------\nfinished process in {end_main-start_main}\n")
    

if __name__ == "__main__":
    main()
