import random
import time


def welcome():  # welcome
    print('-' * 50)
    print('        >>> WELCOME TO HEADS & TAILS <<<')
    print('-' * 50)
    time.sleep(0.5)
    print("> Hi there, Let's start the game!\n")
    time.sleep(1)
    user_name = input("> What is your name?\n")
    time.sleep(0.5)
    print("> Hi {}, Nice to meet you! Now you need to select one of the coin sides..".format(user_name))
    return user_name

def user_selection():
    time.sleep(2)
    user = input("\n> Please enter 'h' for HEADS, 't' for TAILS or 'q' to QUIT:\n")
    if user == 'h':
        user1 = True
        time.sleep(0.5)
        print("> You have selected")
        time.sleep(0.5)
        print(">>> HEADS <<<")
        return user1
    elif user == 't':
        user1 = False
        time.sleep(0.5)
        print("> You have selected")
        time.sleep(0.5)
        print(">>> TAILS <<<")
        return user1
    elif user == 'q':
        time.sleep(0.25)
        print('EXITING in 5..')
        time.sleep(0.25)
        print('4..')
        time.sleep(0.25)
        print('3..')
        time.sleep(0.25)
        print('2..')
        time.sleep(0.25)
        print('1..')
        time.sleep(0.25)
        print("THANK YOU! See you soon..")
        exit()
    else:
        print('Command invalid please try again..')
        user_selection()

def change_selection():
    time.sleep(1)
    change1 = input("> Are you happy with your choice? \nPlease enter 'y' to Continue or 'n' to Change: ".format(welcome1))
    if change1 == 'y':
        return start_game()
    elif change1 == 'n':
        print('\n> Alright {}.. It is not a problem, you can choose it again..\n'.format(welcome1))
        return user_selection()
    else:
        print('> Please enter a valid comand..')
        time.sleep(0.25)
        return user_selection()

def start_game():
    time.sleep(0.5)
    start = input('>> Press ENTER to START <<')

    coin = random.randint(0,1) #coing flip
    time.sleep(1)
    if coin == 0:
        print('> The COIN landed on \n>> HEADS <<')
        coin1 = True
        if coin1 == user:
            time.sleep(3)
            print('>>>> YOU WON! <<<<')
        else:
            print('>>>> YOU LOSE! <<<<')
    if coin == 1:
        print('> The COIN landed on \n> TAILS <')
        coin1 = False
        if coin1 == user:
            time.sleep(3)
            print('>>>> YOU WON! <<<<')
        else:
            print('>>>> YOU LOSE! <<<<')

def play_again():
    again = input("> Hey {}, Do you want to play again? \nEnter 'y' to PLAY AGAIN or 'n' to EXIT".format(welcome1))
    if again == 'y':
        play = True
        user_selection()
    elif again == 'n':
        time.sleep(0.25)
        print('EXITING in 5..')
        time.sleep(0.25)
        print('4..')
        time.sleep(0.25)
        print('3..')
        time.sleep(0.25)
        print('2..')
        time.sleep(0.25)
        print('1..')
        time.sleep(0.25)
        print("THANK YOU! See you soon..")
        exit()
    else:
        print('Command invalid please try again..')
        play_again()

welcome1 = welcome()
user = user_selection()
change = change_selection()
again = play_again()


