# GetTitleClass.py
class GetTitle:
    def __init__(self):
        self.title = ""

    def prompt_for_title(self):
        self.title = input("Please enter the title of the video: ")

    def get_current_title(self):
        return self.title
