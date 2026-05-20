import string


class Алфавит: #Выдаём алфавит англ.
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Алфавит): #вычисоляем кол-во букв 
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog." #Шустрая бурая лисица прыгает через ленивого пса


eng_alphabet = EngAlphabet()
eng_alphabet.print_letters()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('F')) #проверка на наличие буквы F
print(eng_alphabet.is_en_letter('Щ')) #проверка на наличие буквы Щ
print(EngAlphabet.example()) #текст который мы записали
