from word_manager import WordManager
from gui import WordReviewApp


# Main App function
def main(file_path):
    """
    Main function.
    :param file_path:
    :return:
    """
    word_manager = WordManager(file_path)
    app = WordReviewApp(word_manager)
    app.run()