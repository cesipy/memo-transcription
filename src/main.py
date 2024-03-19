import whisper
import logger as l
import os
import preprocess
import time


# globale variable fürs model
model = None
logger = None

def transcribe_audio(path_to_audio: str):
    # es gibt verschiedene modesl, 'base', 'medium', 'large'
    # base funktioniert soweit gut, für evt. bessere performance die anderen 
    global model
    if model == None:
        model = whisper.load_model("medium")  
    result = model.transcribe(path_to_audio)

    return result

def write_to_file(text_body: str, filename: str):
    with open(f"{filename}.txt", "w") as file:
        file.write(text_body)


def process_audio_file(audio_path: str):
    try:
        result = transcribe_audio(audio_path)
        result_string = result["text"]
        #logr.log(result)
        output_filename = preprocess.generate_output_filename(audio_path, "res/converted")
        output_filename = output_filename.replace(".mp3", "")
        full_path_filename = f"res/output/{output_filename}"

        logger.log(f"output filename before writing: {full_path_filename}")

        write_to_file(result_string, full_path_filename)
    except Exception as e:
        logger.log(f"Error processing audio file {audio_path}: {str(e)}")


def process_all_files_in_dir(dir_name: str):
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
    global logger
    logger = l.Logger()
    audio_path = "res/tb-19.03.mp3"
    #process_audio_file(audio_path)
    process_all_files_in_dir("res")
    

if __name__ == "__main__":
    main()
