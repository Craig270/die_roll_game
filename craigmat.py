import random
import time
from prettytable import PrettyTable


def intro():
    print('Welcome to this number counter')
    print('\n')
    print('Input a number and see how long it takes to find')
    print('\n')
    print('Boy! This is smart!')
    print('\n')
    x = int(input('Type 1 for single run or the amount of runs you want to test: (ex. 15)'))
    return x

def bounds():
    x = 0
    y = int(input('Enter how many sides your dice has:'))
    return [x,y]


def pick(x,y):
    player_pick = 0
    print('Enter a number between %d - %d' %(x,y))
    player_pick = int(input('Enter your number here: '))
    while player_pick not in list(range(x, y+1)):
        print('Sorry that will not work!')
        print('Enter a number between %d - %d' % (x, y))
        player_pick = int(input('Enter your number here: '))
    print(f'You entered: {player_pick}')
    return (player_pick)

def rando_gen(x,y):
    return(random.randint(x, y))

def compare_num(x,y):
    if (x==y):
        return 1
    else:
        return 0

def single_run():
    start = time.perf_counter()
    count = 0
    while (1):
        if (compare_num(user_input, rando_gen(bounds_list[0], bounds_list[1]))):
            break
        else:
            count += 1
    # ends clock
    end = time.perf_counter() - start
    print("This looped %d times" % count)
    print("This took %s second(s)" % end)

def multi_run(cycle_count):
    loop_count = []
    time_track = []
    for x in range(cycle_count):
        start = time.perf_counter()
        count = 0
        while (1):
            if (compare_num(user_input, rando_gen(bounds_list[0], bounds_list[1]))):
                break
            else:
                count += 1
        # ends clock
        end = time.perf_counter() - start
        loop_count.append(count)
        time_track.append(end)
    return (loop_count,time_track)

def print_leaderboard_xdee(loop_count, time_count, cycle_style):
    list_order = [i+1 for i in range(cycle_style)]
    #print (list_order)
    #print(loop_count)
    #print(time_count)
    t = PrettyTable([])

    t.add_column("Loop",list_order)
    t.add_column('Tries',loop_count)
    t.add_column('Time', time_count)

    print(t)




cycle_style = intro()
bounds_list = bounds()
user_input = pick(bounds_list[0], bounds_list[1])
if cycle_style == 1:
    single_run()
elif cycle_style !=1:
    count_list,time_list = multi_run(cycle_style)
    print_leaderboard_xdee(count_list,time_list,cycle_style)