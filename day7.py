# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 22:24:04 2025
@author: sena
"""

import random

# Adam çizimleri
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

# Kelime havuzu
word_list = ["camel", "security", "animal", "fenerbahce", "baboon", "cat"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Oyunun başlangıcı
display = ["_"] * word_length
lives = len(stages) - 1
game_over = False
correct_letters = []

print("Adam asmaca oyununa hoş geldin!")

while not game_over:
    guess = input("Bir harf tahmin et: ").lower()

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
                if guess not in correct_letters:
                    correct_letters.append(guess)
    else:
        lives -= 1
        print(f"Yanlış tahmin. Kalan can: {lives}")
        if lives == 0:
            game_over = True
            print("Kaybettin! Doğru kelime:", chosen_word)

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("Tebrikler! Kazandın 🎉")
