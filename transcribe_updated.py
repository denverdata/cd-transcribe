import sys
import whisper

# Accept an audio file path as a command line argument

def main(audio_file_path):
    # Load the Whisper model
    # model = whisper.load_model('base')

    # Transcribe the audio file
    # result = model.transcribe(audio_file_path)
    # print(result['text'])

    if __name__ == '__main__':
        if len(sys.argv) != 2:
            print("Usage: python transcribe.py <audio_file_path>")
            sys.exit(1)
        audio_file_path = sys.argv[1]
        main(audio_file_path)

import os

# Function to split audio filename and extension

def split_filename(filename):
    basename, extension = os.path.splitext(filename)
    return basename, extension

# Transcribe and save output to txt

if __name__ == '__main__':
    audio_file_path = sys.argv[1]
    basename, _ = split_filename(audio_file_path)
    output_file_path = f'{basename}.txt'

    # Load the model as 'medium' to better handle larger files if not already specified
    model = whisper.load_model('medium')

    result = model.transcribe(audio_file_path)
    with open(output_file_path, 'w') as output_file:
        output_file.write(result['text'])
    print(f'Transcription saved to {output_file_path}')
