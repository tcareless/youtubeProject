import os
import subprocess

# Define the directory path and the Whisper command template
directory_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python'
whisper_command_template = 'whisper "{}" --output_format txt --output_dir "/home/tyler/Desktop/youtubeProject/nonCode/txt files/"'

# Change the working directory to the specified path
os.chdir(directory_path)

# List .m4a files in the current directory
m4a_files = [file for file in os.listdir() if file.endswith('.m4a')]

# Run the Whisper command for each .m4a file
for m4a_file in m4a_files:
    # Construct the Whisper command with the actual file name
    whisper_command = whisper_command_template.format(m4a_file)
    
    # Run the Whisper command
    subprocess.run(whisper_command, shell=True)

# Delete all .m4a files in the directory
for m4a_file in m4a_files:
    os.remove(m4a_file)
