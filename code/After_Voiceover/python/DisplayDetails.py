class DisplayDetails:
    def __init__(self, title, thumbnail_path, video_output_dir):
        self.title = title
        self.thumbnail_path = thumbnail_path
        self.video_output_dir = video_output_dir

    def display(self):
        print(f'\nTitle: {self.title}')
        print(f'Thumbnail Path: {self.thumbnail_path}')
        print(f'Video Output Directory: {self.video_output_dir}\n')
