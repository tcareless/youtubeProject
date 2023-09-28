class DisplayDetails:
    def __init__(self, title, thumbnail_path, video_output_dir, description):
        self.title = title
        self.thumbnail_path = thumbnail_path
        self.video_output_dir = video_output_dir
        self.description = description

    def display(self):
        print("\n" + "="*25)
        print("Video Details")
        print("="*25)
        print(f'Title: {self.title}')
        print(f'Thumbnail Path: {self.thumbnail_path}')
        print(f'Video Output Directory: {self.video_output_dir}')
        print(f'Description: {self.description}')
        print("="*25 + "\n")
