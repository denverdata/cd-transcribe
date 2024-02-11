import sys                                                                                                                                                       
import os                                                                                                                                                        
import whisper                                                                                                                                                   
                                                                                                                                                                
def split_filename(filename):                                                                                                                                    
    """                                                                                                                                                          
    Splits a filename into its basename and extension.                                                                                                           
    """                                                                                                                                                          
    basename, extension = os.path.splitext(filename)                                                                                                             
    return basename, extension                                                                                                                                   
                                                                                                                                                                
if __name__ == '__main__':                                                                                                                                       
    # Check for the correct number of arguments                                                                                                                  
    if len(sys.argv) < 2 or len(sys.argv) > 3:                                                                                                                   
        print("Usage: python transcribe.py <audio_file_path> [model_size]")                                                                                      
        sys.exit(1)                                                                                                                                              
                                                                                                                                                                
    audio_file_path = sys.argv[1]                                                                                                                                
    model_size = sys.argv[2] if len(sys.argv) == 3 else 'medium'                                                                                                 
                                                                                                                                                                
    # Split the filename to create the output file name                                                                                                          
    basename, _ = split_filename(audio_file_path)                                                                                                                
    output_file_path = f'{basename}.txt'                                                                                                                         
                                                                                                                                                                
    # Load the Whisper model with the specified size                                                                                                             
    model = whisper.load_model(model_size)                                                                                                                       
                                                                                                                                                                
    # Transcribe the audio file                                                                                                                                  
    result = model.transcribe(audio_file_path)                                                                                                                   
                                                                                                                                                                
    # Save the transcription to a text file                                                                                                                      
    with open(output_file_path, 'w') as output_file:                                                                                                             
        output_file.write(result['text'])                                                                                                                        
    print(f'Transcription saved to {output_file_path}')  