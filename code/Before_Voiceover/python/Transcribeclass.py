# Import necessary libraries and modules
import os
import subprocess

# Import file path variables from filepaths.py
from code.filepaths.filepaths import directory_path, output_dir

# Define the Transcribe class
class Transcribe:
    def __init__(self, directory_path, output_dir):
        self.directory_path = directory_path
        self.output_dir = output_dir
        self.whisper_command_template = 'whisper "{}" --output_format txt --output_dir "{}"  --language English'

    def list_m4a_files(self):
        os.chdir(self.directory_path)
        m4a_files = [file for file in os.listdir() if file.endswith('.m4a')]
        return m4a_files

    def run_whisper(self, m4a_files):
        for m4a_file in m4a_files:
            # Construct the Whisper command with the actual file name
            whisper_command = self.whisper_command_template.format(m4a_file, self.output_dir)
            
            # Run the Whisper command
            subprocess.run(whisper_command, shell=True)

    def delete_m4a_files(self, m4a_files):
        for m4a_file in m4a_files:
            os.remove(m4a_file)

    def transcribe_files(self):
        m4a_files = self.list_m4a_files()
        self.run_whisper(m4a_files)
        self.delete_m4a_files(m4a_files)

# Update the __main__ section to use the imported file path variables
if __name__ == '__main__':
    transcriber = Transcribe(directory_path, output_dir)
    transcriber.transcribe_files()
