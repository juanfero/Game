import random
option=('rock', 'paper', 'scissors')
win_user=0
win_computer=0
rounds=0

while True:

    print('rounds: ', rounds )

    print('win_user: ', win_user)
    print('win_computer: ', win_computer )

    user_option=input('choose option: ')
    rounds+=1

    if not user_option in option:
        print('nombre mal digitado')
        continue

    comput_option=random.choice(option)


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
    
    if win_user==4:
        print('win user game')
        break

    if win_computer==4:
        print('win computer game')
        break






