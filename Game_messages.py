from Card import Card

def show_score(card):
    if card.owner == 'Player':
        print(f'Your hand is worth {card.points}.')
    else:
        print(f'The computer\'s hand is worth {card.points}.')

def winner(player,computer):
    if player.points > computer.points:
        print(f'\nCongratulations! You beat the computer!')
    elif player.points < computer.points:
        print(f'\nSorry, the computer beat you.')