from code.filepaths.filepaths import source_dir, backup_dir  # Importing required paths from filepaths.py
import shutil
import os

class BackupCleanup:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
    
    def move_and_delete_files(self):
        files_moved = 0  # Counter to keep track of the number of files moved
        for filename in os.listdir(self.source_dir):
            full_file_name = os.path.join(self.source_dir, filename)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, self.backup_dir)  # copying file from source to backup directory
                os.remove(full_file_name)  # deleting file from source directory
                files_moved += 1  # Increment the counter when a file is moved and deleted

        if files_moved > 0:
            print(f'Success: {files_moved} files moved and deleted.')
        else:
            print('No files found to move and delete.')
            
# If you want to run the backup and cleanup process independently (optional)
if __name__ == '__main__':
    bc = BackupCleanup(source_dir, backup_dir)
    bc.backup_and_cleanup()
