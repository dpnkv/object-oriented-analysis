from nltk.tokenize import sent_tokenize

class TextProcessing:
    def __init__(self, filename):
        file = open(filename, "r")
        data = file.read()
        self.__characters = len(data)
        self.__words = len(data.split())
        self.__sentences = len(sent_tokenize(data))
        self.__avg_sentence_len = self.__words / self.__sentences

    @property
    def characters(self):
        return self.__characters

    @property
    def words(self):
        return self.__words

    @property
    def sentences(self):
        return self.__sentences

    @property
    def avg_sentence_len(self):
        return self.__avg_sentence_len

text = TextProcessing("text.txt")
print(f"Charactes: {text.characters}")
print(f"Words: {text.words}")
print(f"Sentences: {text.sentences}")
print(f"Average length of sentence (words): {text.avg_sentence_len}")
