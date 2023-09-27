import os
import random
from code.filepaths.filepaths import thumbnail_dir  # Import the thumbnail directory path from filepaths.py

class GetThumbnailClass:
    def __init__(self):
        self.thumbnail_dir = thumbnail_dir  # Directory where thumbnails are stored
        self.thumbnail_path = None  # Variable to store the path of the selected thumbnail

    def choose_random_thumbnail(self):
        try:
            # List all files in the thumbnail directory
            files = [f for f in os.listdir(self.thumbnail_dir) if os.path.isfile(os.path.join(self.thumbnail_dir, f))]
            if not files:
                print("No files found in the specified directory.")
                return None

            # Randomly select a file from the list
            random_file = random.choice(files)

            # Build the complete path to the selected file
            self.thumbnail_path = os.path.join(self.thumbnail_dir, random_file)
            print(f"Thumbnail selected: {self.thumbnail_path}")

        except Exception as e:
            print(f"Error: {e}")

    def get_thumbnail_path(self):
        return self.thumbnail_path

# Usage Example:
if __name__ == "__main__":
    thumbnail_getter = GetThumbnailClass()
    thumbnail_getter.choose_random_thumbnail()
    print(thumbnail_getter.get_thumbnail_path())
