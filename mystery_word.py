def create_board(word):  
    """Let the user know how many letters the secret word contains. Make the board blank so it shows an _ for each letter space that will slowly be filled as user guesses more letters."""
    print(f"This is the create_board function and the value of 'word' is {word}.")
    board_list = []
    for letter in word:
        board_list.append("_")
    print (f"Here is your word to guess: {' '.join(board_list)}")
    return board_list

# below is incomplete so I am commenting this out for now
# I left what was here so I could go back and rework from where started
# def show_board(word):
#         display_board = " ".join(board_list)
#     print (f"Here is your word to guess: {display_board}. It has {len(word)} letters which is pretty evident if you count the spaces.")

# below gets one user's guess, no parameters have to be given
def get_user_guess():
    """Ask use to guess a letter then store it and display it"""
    guess = input("Guess your letter: ")
    return guess

def show_board(word, board, correct_list):
    for letter in correct_list:
            for idx in range(len(word)):
                if word[idx] == letter:
                    board[idx] = letter
    print(" ".join(board))

# def already_guessed(letter):


def play_game():
    """All game play happens in this function"""
    word_to_guess = 'dream'.upper()
    game_board = create_board(word_to_guess)
    correct_guesses = []
    incorrect_guesses = []
    number_of_incorrect_guesses = 0
    all_guesses = [correct_guesses + incorrect_guesses]
    how_many_guesses = 8
    # make a loop that stops when word is guessed or user has no more guesses
    while len(incorrect_guesses) < how_many_guesses and "_" in game_board:
        new_guess = get_user_guess().upper()
        if new_guess == '':
            print("You forgot to enter a letter. Try again.")
        elif new_guess in correct_guesses or incorrect_guesses:
            print(f"You have already guessed '{new_guess}'. Pay attention!")
        elif new_guess in word_to_guess:
            correct_guesses.append(new_guess)
            print(f"Cool Nastredamus bc '{new_guess}' is in it!")
            print(correct_guesses)
        else:
            incorrect_guesses.append(new_guess)
            number_of_incorrect_guesses += 1
            print(f"Sorry, no love on the letter {new_guess}. {how_many_guesses - number_of_incorrect_guesses} guesses remaining.")
            print("These are the letters you have guessed so far that are not in the word:")
            print(incorrect_guesses)
        show_board(word_to_guess, game_board, correct_guesses)
    if "_" not in game_board:
        print("Excellent. Vanna would be proud.")

if __name__ == "__main__":
    play_game()


