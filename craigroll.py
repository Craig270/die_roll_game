import random 

player_pick = 0
rolls = 0
print('\n')
print('Welcome to this super simple 100 Sided Dice game!')
print('\n')
print('See how many times it takes you to roll your number on a 100 Sided Dice!')
print('\n')

while player_pick not in list(range(1,101)):
        player_pick = int(input('Enter your number here (1-100): '))
print('\n')
print(f'\tYou entered: {player_pick}')
print('\n')

rand_num = random.randint(1, 100)

while player_pick != rand_num:
	rand_num = random.randint(1,100)
	print('The 100 Sided Dice rolled %d' %rand_num)
	rolls += 1
print('\n')
print(f'It took {rolls} rolls to get to your number {player_pick}')