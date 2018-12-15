import random
from _operator import index


class User:

    def __init__(self):
        self.secret_word = self.pick_random_word()
        self.word_masked = ['_' for letter in self.secret_word]

    def get_words(self):
        with open('words_list2.txt', 'r') as f:
            list_word = [line.strip().lower() for line in f.readlines()]
            return list_word

    def pick_random_word(self):
        get_list_word = self.get_words()
        while True:
            random_word = random.choice(get_list_word)
            if len(random_word) >= 6:
                return random_word

    def show_menu(self):
        # user_chance = 10
        menu = input('''
        Menu:
        press (a) to play
        press (b) to exit
        ''')
        while menu == "a":
            new_letter = self.get_letter()
            print(new_letter)

    def get_letter(self):
        letter_input = input("Please tape a letter.")

        if len(letter_input)==1:
            if letter_input.isalpha():
                for index, letter in enumerate(self.secret_word):
                    if letter_input == letter:
                        self.word_masked[index] = letter_input



na = User()
print(na.secret_word)
print(na.word_masked)

while "_" in na.word_masked:
    na.get_letter()
    print(' '.join(na.word_masked))



print(na.word_masked)



#
# my_word = User()
# print(my_word.secret_word)
#
# menu = User()
# print(menu.show_menu())
#
# letter = User()
# print(letter.get_letter())
#

