import ezodf
import random
from datetime import datetime
import tkinter as tk
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\georg\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\georg\AppData\Local\Programs\Python\Python313\tcl\tk8.6'


# Definování intervalů opakování v dnech
INTERVALS = [1, 3, 7, 10, 15, 30, 60, 90]


# Třída pro práci se slovíčky a kontrolou opakování (Separation of Concerns)
class WordManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self.load_words_from_ods()
        self.words_to_review = []

    def load_words_from_ods(self):
        ezodf.config.set_table_expand_strategy('all')
        doc = ezodf.opendoc(self.file_path)
        sheet = doc.sheets[0]  # První list v souboru
        words = []

        for row in sheet.rows():
            if row[0].value and row[1].value and row[2].value:
                try:
                    date_added = datetime.strptime(row[0].value, '%Y-%m-%d')
                    spanish_word = row[1].value
                    czech_translation = row[2].value
                    words.append((date_added, spanish_word, czech_translation))
                except ValueError:
                    # Přeskočit špatně formátované datum
                    continue
        return words

    def check_words_for_review(self):
        today = datetime.now()
        self.words_to_review.clear()

        for date_added, spanish_word, czech_translation in self.words:
            days_since_added = (today - date_added).days
            if any(days_since_added == interval for interval in INTERVALS):
                self.words_to_review.append((spanish_word, czech_translation))

    def get_random_words(self, count=50):
        random.shuffle(self.words_to_review)
        return self.words_to_review[:count]


# Třída pro uživatelské rozhraní (GUI)
class WordReviewApp:
    def __init__(self, word_manager):
        self.word_manager = word_manager
        self.words_to_test = []
        self.current_word_index = 0
        self.current_word = None
        self.is_showing_czech = True

        # Inicializace okna
        self.root = tk.Tk()
        self.root.title("Opakování slovíček")
        self.root.geometry("600x300")

        # Centrování okna na obrazovce
        self.center_window()

        # Vytvoření prvků GUI
        self.label_word = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.label_word.pack(expand=True, padx=20, pady=20)

        self.label_progress = tk.Label(self.root, text="Pokrok: 0/50", font=("Helvetica", 12))
        self.label_progress.pack(pady=10)

        # Bindování mezerníku pro zobrazení dalšího slova
        self.root.bind("<space>", self.handle_space_press)

    def center_window(self):
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (300 // 2)
        self.root.geometry(f"600x300+{x}+{y}")

    def start_review(self):
        self.word_manager.check_words_for_review()
        self.words_to_test = self.word_manager.get_random_words()
        if not self.words_to_test:
            self.label_word.config(text="Dnes není žádné slovo k opakování.")
            return

        self.current_word_index = 0
        self.is_showing_czech = True
        self.show_next_word()

    def show_next_word(self):
        if self.current_word_index >= len(self.words_to_test):
            self.label_word.config(text="Konec opakování.")
            return

        # Zobrazit české slovo a aktualizovat pokrok
        self.current_word = self.words_to_test[self.current_word_index]
        czech_word = self.current_word[1]  # český překlad
        self.label_word.config(text=f"CZ: {czech_word}")
        self.label_progress.config(text=f"Pokrok: {self.current_word_index + 1}/{len(self.words_to_test)}")

    def show_spanish_translation(self):
        spanish_word = self.current_word[0]  # španělské slovo
        self.label_word.config(text=f"ES: {spanish_word}")

    def handle_space_press(self, event):
        if self.is_showing_czech:
            self.show_spanish_translation()
        else:
            self.current_word_index += 1
            self.show_next_word()

        self.is_showing_czech = not self.is_showing_czech

    def run(self):
        self.start_review()
        self.root.mainloop()


# Hlavní funkce aplikace
def main(file_path):
    word_manager = WordManager(file_path)
    app = WordReviewApp(word_manager)
    app.run()


if __name__ == "__main__":
    file_path = 'slovnik.ods'  # Změňte na cestu ke svému souboru
    main(file_path)
