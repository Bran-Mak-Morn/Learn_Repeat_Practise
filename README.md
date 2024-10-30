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
```bash
## Usage
Load your words: Update the data.csv file with Spanish words and their Czech translations.
Run the application:
```bash
python word_review_app.py
```bash
Review Words: The application will display words for review based on the intervals defined in the word_manager.py. Use the space bar to toggle between the Czech and Spanish translations, and navigate through the words.

## Project Highlights
Dynamic Word Review: The application checks the dates words were added and presents them for review based on specific intervals, ensuring effective learning.
Shuffling for Variety: Words are shuffled before review to provide a varied learning experience, preventing memorization based solely on order.
AI-Assisted Development: This project was developed entirely through instructions (prompts) provided to an AI coding tool, demonstrating the potential of AI in the coding process and marking a new era of programming.

Acknowledgments
This project exemplifies the future of coding with AI agents, showcasing how technology can assist developers in creating functional applications without traditional coding methods.

vbnet

### Notes on the README Structure:
- **Clear Sections**: The README is structured with clear headings to help users navigate easily.
- **Emphasis on AI Assistance**: It highlights the innovative aspect of using AI for coding, as you requested.
- **Usage Instructions**: Provides straightforward instructions on how to set up and use the application, making it user-friendly.

Feel free to modify any sections or add any additional details as necessary! If you have any further requests or need adjustments, just let me know!
