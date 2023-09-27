class DescriptionGetter:
    def __init__(self):
        self.description = ""  # Initialize an empty description

    def prompt_for_description(self):
        self.description = input("Please enter the video description: ")

    def get_description(self):
        return self.description


# Usage:
if __name__ == "__main__":
    description_getter = DescriptionGetter()
    description_getter.prompt_for_description()
    print(f"...thank you for entering a description...")
