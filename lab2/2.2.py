from nltk.tokenize import sent_tokenize
import os.path

class TextProcessing:
    """Class that do statistical processing of a text file."""
    def __init__(self, filename):
        self.filename = filename

    def get_chars(self):
        """Get number of characters in a file."""
        with open(self.filename, "r") as file:
            if not os.path.isfile(self.filename):
                raise FileNotFoundError
            self.__characters = 0
            for line in file.readlines():
                self.__characters += len(line)
            return self.__characters

    def get_words(self):
        """Get number of words in a file."""
        with open(self.filename, "r") as file:
            if not os.path.isfile(self.filename):
                raise FileNotFoundError
            self.__words = 0
            for line in file.readlines():
                self.__words += len(line.split())
            return self.__words

    def get_sentences(self):
        """Get number of sentences in a file."""
        with open(self.filename, "r") as file:
            if not os.path.isfile(self.filename):
                raise FileNotFoundError
            self.__sentences = 0
            for line in file.readlines():
                self.__sentences += len(sent_tokenize(line))
            return self.__sentences


text = TextProcessing("text.txt")
print(f"Charactes: {text.get_chars()}")
print(f"Words: {text.get_words()}")
print(f"Sentences: {text.get_sentences()}")
