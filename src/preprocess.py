import pydub
import subprocess

import os

def convert_all_files_to_wav(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith(".m4a"):  # or any other format you want to convert from
            print(f"filename: {filename}\n {os.path.join(directory, filename)}\n")
            convert_to_wav(os.path.join(directory, filename))


def convert_to_wav(file_path: str):
    relative_path = os.path.relpath(file_path, 'res')
    output_file_path = relative_path.replace(" ", "-").replace(".m4a", ".wav")

    print(relative_path)
    print(output_file_path)
    subprocess.call(['ffmpeg', '-i', 
                     f'{file_path}',
                     f'res/converted/{output_file_path}'])
    print("finished conversion")
    

convert_all_files_to_wav("res")