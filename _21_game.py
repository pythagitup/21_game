from Card import Card
from Game_messages import show_score, winner

print('Let\'s play 21!\n\nPress enter for your starting hand.')
input()

play = Card()

play.draw(2)
play.score()
show_score(play)

while True:
    choice = input('\nWould you like to stay or hit? ')

    if choice.title() == 'Hit':
        play.draw(1)
        play.score()
        if play.points > 21:
            print('Bust!!')
            play.points = 0
            break
        else:
            show_score(play)
    if choice.title() == 'Stay':
        show_score(play)
        break

print('\nIt\'s the computer\'s turn now!')
input()

ai_play = Card('Computer')

ai_play.draw(2)
ai_play.score()
show_score(ai_play)
input()

while True:
    if ai_play.points <= play.points:
        print(f'The computer hits.')
        ai_play.draw(1)
        ai_play.score()
        if ai_play.points > 21:
            print('The computer goes bust!!')
            ai_play.points = 0
            break
        else:
            show_score(ai_play)
    else:
        print(f'The computer stays.')
        break
    input()

winner(play,ai_play)