import argparse                                                                                                                                                  
import os                                                                                                                                                        
import whisper                                                                                                                                                   
                                                                                                                                                                
def split_filename(filename):                                                                                                                                    
    basename, extension = os.path.splitext(filename)                                                                                                             
    return basename, extension                                                                                                                                   
                                                                                                                                                                
def main():                                                                                                                                                      
    parser = argparse.ArgumentParser(description='Transcribe audio files using OpenAI\'s Whisper model.')                                                        
    parser.add_argument('audio_file_path', type=str, help='Path to the audio file to transcribe.')                                                               
    parser.add_argument('--model_size', type=str, default='medium', choices=['tiny', 'base', 'small', 'medium', 'large'], 
                        help='Size of the Whisper model to use for transcription.')                                                                                                                                                
                                                                                                                                                                
    args = parser.parse_args()                                                                                                                                   
                                                                                                                                                                
    audio_file_path = args.audio_file_path                                                                                                                       
    model_size = args.model_size                                                                                                                                 
                                                                                                                                                                
    basename, _ = split_filename(audio_file_path)                                                                                                                
    output_file_path = f'{basename}.txt'                                                                                                                         
                                                                                                                                                                
    model = whisper.load_model(model_size)                                                                                                                       
    result = model.transcribe(audio_file_path)                                                                                                                   
                                                                                                                                                                
    with open(output_file_path, 'w') as output_file:                                                                                                             
        output_file.write(result['text'])                                                                                                                        
                                                                                                                                                                
    print(f'Transcription saved to {output_file_path}')                                                                                                          
                                                                                                                                                                
if __name__ == '__main__':                                                                                                                                       
    main()   