import pydub
import subprocess

import os

def convert_all_files_to_wav(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith(".m4a"):  # or any other format you want to convert from
            convert_to_wav(os.path.join(directory, filename))


def convert_to_wav(file_path: str):
    file_path_without_extensions = file_path.replace(" ", "-").replace("\ ", "-").replace(".m4a", ".wav")
    print(file_path_without_extensions)
    subprocess.call(['ffmpeg', '-i', 
                     f'res/{file_path}',
                     f'res/output/{file_path_without_extensions}'])
    print("finished conversion")
    

convert_all_files_to_wav("res")