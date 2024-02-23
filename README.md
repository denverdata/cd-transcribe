# Transcribe App

The Transcribe App is a simple utility for converting audio files into text. It leverages the powerful Whisper model to accurately transcribe spoken words into written form. This can be particularly useful for generating transcripts of recordings, interviews, or any audio content that you wish to have in text format.

## Installation

To use the Transcribe App, you need to have Python installed on your machine, as well as the necessary Python packages. Follow these steps to set up:

1. Clone this repository or download the contents of the `transcribe` directory to your local machine. 

    GitHub Repo: https://github.com/denverdata/cd-transcribe
2. Ensure that you have Python installed. The app has been tested with Python 3.11.
3. Setup and your virtual environment.
    ```bash
    python -m venv python3.11 cdt
    ```
    ```bash
    source cdt/bin/activate
    ```
4. Install the required packages using pip. Run the following command in the terminal:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Be sure to activte your virtual env if you have not already

On MacOS:
```
source cdt/bin/activate
```

To transcribe an audio file, navigate to the `transcribe` directory in your terminal and run:

```bash
python transcribe.py <audio_file_path> --model_size "tiny"
```

Replace `<audio_file_path>` with the path to the audio file you want to transcribe. The script will generate a text file in the same directory as the audio file, named identically but with a `.txt` extension.

For example, for the audio file named `./testdata/testaudio.m4a`, the transcript will be saved in a file called `./testdata/testaudio.txt`.

## Input cFormats

CD Transcribe trasnlates a variety of audio and video formats.