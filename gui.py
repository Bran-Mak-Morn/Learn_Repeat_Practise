import tkinter as tk


class WordReviewApp:
    """
    Class for GUI.
    """
    def __init__(self, word_manager):
        self.word_manager = word_manager
        self.words_to_review = []
        self.current_word_index = 0
        self.is_showing_czech = True
        self.batch_start_index = 0
        self.batch_size = 50

        # Window setup
        self.root = tk.Tk()
        self.root.title("Your Spanish Words to Review")
        self.root.geometry("600x300")

        # Window centering
        self.center_window()

        # Labels
        self.label_word = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.label_word.pack(expand=True, padx=20, pady=20)

        self.label_progress = tk.Label(self.root, text="Progress: 0/50", font=("Helvetica", 12))
        self.label_progress.pack(pady=10)

        # Binding for space key
        self.root.bind("<space>", self.handle_space_press)

        # Buttons
        self.button_next_batch = tk.Button(self.root, text="Another Group of 50", fg="green", font=("Helvetica", 10, "bold"),
                                           command=self.load_next_batch, width=17)
        self.button_next_batch.pack(side="left", padx=30, pady=15)

        self.button_random_words = tk.Button(self.root, text="Random Words", fg="blue", font=("Helvetica", 10, "bold"),
                                             command=self.load_random_words, width=17)
        self.button_random_words.pack(side="left", padx=30, pady=15)

        self.button_exit = tk.Button(self.root, text="I'm Done", fg="red", font=("Helvetica", 10, "bold"),
                                     command=self.root.quit, width=17)
        self.button_exit.pack(side="right", padx=30, pady=15)

    def center_window(self):
        """
        Center window on screen.
        """
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (300 // 2)
        self.root.geometry(f"600x300+{x}+{y}")

    def start_review(self):
        """
        Start review process.
        """
        self.word_manager.check_words_for_review()
        self.load_next_batch()

        if not self.words_to_review:
            self.set_label_message("No more words to review today :)")
            return

        self.current_word_index = 0
        self.is_showing_czech = True
        self.show_next_word()

    def show_next_word(self):
        """
        Show next word. If there are no more words, show message.
        """
        if self.current_word_index >= len(self.words_to_review):
            self.set_end_of_review_message()
            return

        # Show Czech word and update progress
        czech_word = self.words_to_review[self.current_word_index][1]  # Czech translation
        self.label_word.config(text=f"CZ: {czech_word}")
        self.label_progress.config(text=f"Progress: {self.current_word_index + 1}/{len(self.words_to_review)}")

    def show_spanish_translation(self):
        """
        Show Spanish translation.
        """
        spanish_word = self.words_to_review[self.current_word_index][0]  # Spanish word
        self.label_word.config(text=f"ES: {spanish_word}")

    def handle_space_press(self, event):
        """
        Handle space press. Switch between showing Spanish and Czech translation.
        """
        if self.is_showing_czech:
            self.show_spanish_translation()
        else:
            self.current_word_index += 1
            self.show_next_word()

        self.is_showing_czech = not self.is_showing_czech

    def load_next_batch(self):
        """
        Load the next batch of words for review.
        """
        self.words_to_review = self.word_manager.get_next_batch(self.batch_start_index, self.batch_size)

        if not self.words_to_review:
            self.set_label_message("No more words to review today :)")
            self.button_next_batch.config(state=tk.DISABLED)  # Disable next batch button if no more words
            return

        self.batch_start_index += self.batch_size  # Update start index for the next batch
        self.current_word_index = 0
        self.is_showing_czech = True
        self.show_next_word()

    def load_random_words(self):
        """
        Load 50 random words using WordManager's select_random_words_for_review method.
        """
        self.word_manager.select_random_words_for_review()
        self.words_to_review = self.word_manager.words_to_review

        if not self.words_to_review:
            self.set_label_message("No words available for random selection.")
            return

        self.current_word_index = 0
        self.is_showing_czech = True
        self.show_next_word()

    def set_label_message(self, message: str):
        """
        Set the message for the word label.
        :param message: The message to display in the label.
        """
        self.label_word.config(text=message)

    def set_end_of_review_message(self):
        self.set_label_message("The End of the Review")

    def run(self):
        """
        Run GUI application.
        """
        self.start_review()
        self.root.mainloop()
