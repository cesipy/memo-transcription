import pydub
import subprocess
import logger as l


import os
logger = l.Logger()

def convert_all_files_to_wav(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith(".m4a"):  # or any other format you want to convert from
            print(f"filename: {filename}\n {os.path.join(directory, filename)}\n")
            convert_to_wav(os.path.join(directory, filename))

def generate_output_filename(file_path: str, dir_path:str):
    relative_path = os.path.relpath(file_path, dir_path)
    output_file_path = relative_path.replace(" ", "-").replace(".m4a", ".wav")

    return output_file_path

def convert_to_wav(file_path: str):
    output_file_path = generate_output_filename(file_path, "res")
    output_file_path = f"res/converted/{output_file_path}"

    subprocess.call(['ffmpeg', '-i', 
                     f'{file_path}',
                     f'{output_file_path}'])
    #logger.log("finished conversion")
    return output_file_path
    
