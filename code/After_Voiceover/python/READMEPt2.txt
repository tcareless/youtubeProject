---

# Automated Video Production and YouTube Uploading

This project comprises a set of Python scripts that automate various aspects of video production, right from title selection, thumbnail generation, video building, description entry, and uploading the produced video to YouTube. It also includes a Backup and Cleanup utility for managing files.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Google API client library
- MoviePy
- PyDub
- A Google Account with YouTube Data API v3 enabled and OAuth 2.0 credentials set up.

### Installation

1. Clone the repository to your local machine.
```bash
git clone https://github.com/your-repo/automated-video-production.git
cd automated-video-production
```
2. Install the required Python packages.
```bash
pip install -r requirements.txt
```
3. Create a `credentials.json` file for your Google API credentials and place it in the `code/filepaths/` directory.

### Directory Structure

```
.
├── code
│   ├── After_Voiceover
│   │   ├── python
│   │   │   ├── BackupCleanup.py
│   │   │   ├── DescriptionGetter.py
│   │   │   ├── DisplayDetails.py
│   │   │   ├── GetThumbnailClass.py
│   │   │   ├── GetTitleClass.py
│   │   │   ├── VideoBuilderClass.py
│   │   │   └── YoutubeUploader.py
│   │   └── ...
│   ├── filepaths
│   │   └── filepaths.py
│   └── ...
└── README.md
```

## Usage

1. Run the main script to start the automated video production process:
```bash
python main.py
```
2. Follow the on-screen prompts to enter the video title, choose a thumbnail, enter a description, and other actions as per your requirements.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- The project uses the YouTube Data API v3 for uploading videos to YouTube.
- Video processing is handled by the MoviePy and PyDub libraries.

---

