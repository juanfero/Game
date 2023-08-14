import random

def opciones():
    option=('rock', 'paper', 'scissors')
    user_option=input('choose option: ')
    comput_option=random.choices(option)
    print('User option =>', user_option)
    print('Computer option =>', comput_option)
    return user_option,comput_option
 

def rules(user_option,comput_option,win_user, win_computer):
    if user_option==comput_option:
        print('empate')
    elif user_option=='rock':
        if comput_option=='scissors':
            win_user+=1
        else:
            win_computer+=1

    elif user_option=='paper':
        if comput_option=='rock':
            win_user+=1
        else:
            win_computer+=1

    elif user_option=='scissors':
        if comput_option=='paper':
            win_user+=1
        else:
            win_computer+=1
    return win_user,win_computer
def run():

    win_user=0
    win_computer=0
    rounds=0

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('computer_wins', win_computer)
        print('user_wins', win_user)
        rounds+=1
        print('rounds: ', rounds )

        user_option, comput_option = opciones()
        win_user, win_computer = rules(user_option, comput_option, win_user, win_computer)

        if win_computer==2:
            print('win computer game')
            break

        if win_user==2:
            print('win user game')
            break
run()