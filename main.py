# python code for rock paper scissor game

import random


def game_initialize():
    game_rounds = int(input('Enter the number of rounds\n'))

    computer_score = 0
    person_score = 0
    game_aborted = False
    for game_round in range(game_rounds):
        game_result = run_game()
        if game_result == -1:
            game_aborted = True
            break
        else:
            computer_score += game_result[0]
            person_score += game_result[1]

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


def run_game():
    game_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
    invalid_moves = 0
    player_choice = ''
    comp_score = 0
    person_score = 0
    for i in range(5):
        player_choice = input('Enter your move\n')
        if player_choice not in game_dict.values():
            print('Invalid Move')
            invalid_moves += 1
            if invalid_moves == 4:
                return -1
        else:
            break

    computer_choice = random.randint(1, 3)
    computer_choice = game_dict.get(computer_choice)
    print(f'computer played : {computer_choice}')

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

    return comp_score, person_score


game_initialize()
