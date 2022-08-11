# python code for rock paper scissor game

import random


# Function to initiate the game
def game_initialize():
    game_rounds = int(input('Enter the number of rounds\n'))

    computer_score = 0
    person_score = 0
    game_aborted = False

    # Run the game till all the rounds are exhausted
    for game_round in range(game_rounds):
        game_result = run_game()
        if game_result == -1:
            game_aborted = True
            break
        else:
            computer_score += game_result[0]
            person_score += game_result[1]

    # Conditions to show the result
    if game_aborted:
        print("Game Aborted!")
        return 0
    if computer_score > person_score:
        print("Computer won\n")
    elif computer_score == person_score:
        print("Game Tied\n")
    else:
        print("You Won\n")
    print(f'Scoring: \n' + f'You: {person_score}\n' + f'Computer: {computer_score}\n')


# Function to run the game - core logic
def run_game():
    game_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}  # The choices
    invalid_moves = 0
    player_choice = ''
    comp_score = 0
    person_score = 0
    # Giving 5 chances if invalid inputs are given
    for i in range(5):
        player_choice = input('Enter your move\n')
        if player_choice not in game_dict.values():
            print('Invalid Move')
            invalid_moves += 1
            if invalid_moves == 4:
                return -1
        else:
            break

    # Logic for computer's move
    computer_choice = random.randint(1, 3)
    computer_choice = game_dict.get(computer_choice)
    print(f'computer played : {computer_choice}')

    # Logic for deciding the score
    if computer_choice == 'Rock' and player_choice == 'Paper':
        person_score += 1
    elif computer_choice == 'Rock' and player_choice == 'Scissor':
        comp_score += 1
    elif computer_choice == 'Paper' and player_choice == 'Scissor':
        person_score += 1
    elif computer_choice == 'Paper' and player_choice == 'Rock':
        comp_score += 1
    elif computer_choice == 'Scissor' and player_choice == 'Paper':
        comp_score += 1
    elif computer_choice == 'Scissor' and player_choice == 'Rock':
        person_score += 1
    else:
        pass

    # Returning the score tuple
    return comp_score, person_score


# Start the game
game_initialize()
