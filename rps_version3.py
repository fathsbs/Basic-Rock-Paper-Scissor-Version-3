from random import randint
print('Rock...')
print('Paper...')
print('Scissor...')

# input player
player = input('Player, make your move: ').lower() 
# lower is method for making word to be lowercase

# logic for computer choosing its move
rand_num = randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissor'

#logic for rock, paper, and scissor
if player == 'rock' or player == 'paper' or player == 'scissor':
    print(f'Computer plays {computer}')
    # same move
    if player == computer:
        # logic if they are using same move
        print('it\'s a tie')
    # rock 
    elif player == 'rock':
        if computer == 'scissor':
            # logic rock vs scissor
            print('player wins!')
        else:
            # logic rock vs paper
            print('computer wins!')
    # paper
    elif player == 'paper':
        if computer == 'rock':
            # logic paper vs rock
            print('player wins!')
        else:
            # logic paper vs scissor
            print('computer wins!')
    # scissor
    elif player == 'scissor':
        if computer == 'paper':
            # logic scissor vs paper
            print('player wins!')
        else:
            # logic scissor vs rock
            print('computer wins!')
else:
    # logic if the input are betweem rock, paper, and scissor
    print('Please enter invalid move!')
