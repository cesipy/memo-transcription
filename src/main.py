import whisper


# globale variable fürs model
model = None

def transcribe_audio(path_to_audio: str):
    # es gibt verschiedene modesl, 'base', 'medium', 'large'
    # base funktioniert soweit gut, für evt. bessere performance die anderen 
    global model
    if model == None:
        model = whisper.load_model("medium")  
    result = model.transcribe(path_to_audio)

    return result

def write_to_file(text: str):
    with open("res/output/output.txt", "w") as file:
        file.write(text)


def process_audio_file(audio_path: str):
    #logr = logger.Logger()
    try:
        result = transcribe_audio(audio_path)
        result_string = result["text"]
        #logr.log(result)
        write_to_file(result_string)
    except Exception as e:
        #logr.log(f"Error processing audio file {audio_path}: {str(e)}")
        print(f"Error processing audio file {audio_path}: {str(e)}")


def main():
    audio_path = "res/tb-19.03.mp3"
    process_audio_file(audio_path)
    

if __name__ == "__main__":
    main()
