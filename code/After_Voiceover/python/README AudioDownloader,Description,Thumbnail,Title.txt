# Project Title

This project encompasses a suite of tools aimed at automating various aspects of video creation and management. These include downloading audio from Google Drive, picking thumbnails for videos, setting titles and descriptions for videos, among others. Below is a breakdown of the essential Python classes involved in achieving these functionalities:

## Table of Contents

- [1. AudioDownloader Class](#audio-downloader-class)
- [2. DescriptionGetter Class](#description-getter-class)
- [3. GetThumbnailClass](#get-thumbnail-class)
- [4. GetTitle Class](#get-title-class)
- [5. Setup](#setup)
- [6. Usage](#usage)

## Audio Downloader Class

The `AudioDownloader` class is designed to interact with Google Drive to download audio files. It authenticates access to Google Drive, searches for a specific folder, downloads all files within that folder, and optionally deletes the files from Drive post-download.

### Attributes:

- `token_path`: Path to the token file for authentication.
- `credentials_path`: Path to the credentials file for authentication.
- `voiceover_output_dir`: Directory where the downloaded files will be saved.

### Methods:

- `authenticate`: Handles authentication to Google Drive.
- `download_audio`: Downloads audio files from a specified folder in Google Drive.

```python
# Usage Example:
audio_downloader = AudioDownloader(token_path, credentials_path, voiceover_output_dir)
audio_downloader.download_audio()
```

## Description Getter Class

The `DescriptionGetter` class is a straightforward class for obtaining a description via user input.

### Attributes:

- `description`: Holds the description entered by the user.

### Methods:

- `prompt_for_description`: Prompts the user to enter a description.
- `get_description`: Returns the description entered by the user.

```python
# Usage Example:
description_getter = DescriptionGetter()
description_getter.prompt_for_description()
```

## Get Thumbnail Class

The `GetThumbnailClass` randomly selects a thumbnail image from a specified directory.

### Attributes:

- `thumbnail_dir`: Directory where thumbnail images are stored.
- `thumbnail_path`: Path of the selected thumbnail.

### Methods:

- `choose_random_thumbnail`: Randomly selects a thumbnail from the specified directory.
- `get_thumbnail_path`: Returns the path of the selected thumbnail.

```python
# Usage Example:
thumbnail_getter = GetThumbnailClass()
thumbnail_getter.choose_random_thumbnail()
```

## Get Title Class

The `GetTitle` class obtains a title for the video via user input.

### Attributes:

- `title`: Holds the title entered by the user.

### Methods:

- `prompt_for_title`: Prompts the user to enter a title.
- `get_current_title`: Returns the title entered by the user.

```python
# Usage Example:
title_getter = GetTitle()
title_getter.prompt_for_title()
```

## Setup

Ensure all necessary libraries and modules are installed. Update the `filepaths.py` with the appropriate paths to your directories and credential files.

## Usage

The classes can be utilized independently or integrated into larger workflows as per the project requirements. Below are basic examples of how to instantiate and use each class:

```python
audio_downloader = AudioDownloader(token_path, credentials_path, voiceover_output_dir)
audio_downloader.download_audio()

description_getter = DescriptionGetter()
description_getter.prompt_for_description()

thumbnail_getter = GetThumbnailClass()
thumbnail_getter.choose_random_thumbnail()

title_getter = GetTitle()
title_getter.prompt_for_title()
```

These classes serve as the building blocks for more complex operations within the video management project.

---

The breakdown above encapsulates the core functionalities provided by the script files shared. Each class is designed to handle a specific aspect of the project, making the codebase modular and easy to manage or expand.