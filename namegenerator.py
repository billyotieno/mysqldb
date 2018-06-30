import random
import string

class RandomName:

    def __init__(self):
        self.__VOWELS = "aeiou"
        self.__CONSONANTS = "".join(set(string.ascii_lowercase) - set(self.__VOWELS))

    def generate_word(self, length):
        word = ""
        for i in range(length):
            if i % 2 == 0:
                word += random.choice(self.__CONSONANTS)
            else:
                word += random.choice(self.__VOWELS)
        return word