# Spanish-Czech Word Review App

A Python project for reviewing and learning Spanish words with their Czech translations, utilizing a graphical user interface built with Tkinter.

## Overview
This application allows users to review Spanish words along with their Czech translations. Words are added to the application from a CSV file, and users can review them based on predefined intervals for effective learning.

## Technologies
- Python for backend logic
- Tkinter for the GUI
- CSV for data management

## License
This project is under the MIT license. Libraries and modules have their own licenses:

- Tkinter: Python Software Foundation License
- CSV: Python Software Foundation License

## Files
- `word_manager.py`: Contains the `WordManager` class for managing words from a CSV file, including loading, checking intervals for review, and retrieving words.
- `word_review_app.py`: Implements the `WordReviewApp` class for the GUI, allowing users to review words and manage their learning experience.
- `data.csv`: Sample CSV file containing Spanish words and their Czech translations along with the dates they were added.

## Setup

### Prerequisites
- Python 3.7+

### Required Python packages
- Tkinter (comes with standard Python distribution)
- Other dependencies specified in `requirements.txt` (if applicable)

### Installation
Install packages:
```bash
pip install -r requirements.txt
