import random

# Define the game choices with distinct ASCII art
rock = '''
    _______
---'   ___)____
          ______)
         _______)
        _______)
---.__________)
'''

paper = '''
    _______
---'   ___)____
          ________)
         _________)
        _________)
---.____________)
'''

scissors = '''
    _______
---'   ___)____
          __________)
       __________)
      ________)
---.__________)
'''

# Create a list of game images
game_images = [rock, paper, scissors]

# Get the user's selection
user_choice = int(input("Ne seçiyorsun? Taş için 0, Kağıt için 1 veya Makas için 2 yaz: "))

print("\n---") 

if 0 <= user_choice < 3:
    print(f"Sen seçtin:\n{game_images[user_choice]}")

    # Generate the computer's random choice
    computer_choice = random.randint(0, 2)
    print(f"\nBilgisayar seçti:\n{game_images[computer_choice]}")

    # Determine the outcome of the game
    if user_choice == computer_choice:
        print("\nBerabere!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("\nKazandın!")
    else:
        print("\nKaybettin!")
else:
    print("\nGeçersiz seçim! Lütfen 0, 1 veya 2 yazmalısın.")

print("\n---") 