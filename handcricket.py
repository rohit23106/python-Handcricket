import random
import moviepy
from moviepy.editor import *
import pygame
from PIL import Image
clip = VideoFileClip('C:/Users/majet/Downloads/28275775-preview.mp4')
clip.preview()
pygame.quit()
img = Image.open('audio/image.png')
img.show()
print("Welcome to Handcricket Online .... Have Fun Lets start playing!")
user = input("Enter name:")
pygame.init()
pygame.mixer.music.load('C:/Users/majet/Downloads/ipl_remix.mp3')
pygame.mixer.music.play()
# RULES
print('''The rules of the game are:
      1. There will be a toss between you and the computer, you have to chose either odd or even, after that you should put a number between 1 to 10
    if the sum of your and the computer's number is odd or even, accordingly to what you have choosen you will either win or loss the toss.
    If you win the toss you can either bat or bowl, and the same thing will happen with the computer.
    2. If you are batting then you have to put a number between 1 to 10 to score runs, if the number you have put and the number computer has put is same
    the you will be declared out, if not then you can continue to bat till you get out and it is a 10 over game
    3. After you finish batting, you have to bowl and defend your score and get the computer out be chosing the same number as the computer
    4.Hope you have fun
    5.It is a 2 over match they are 12 balls''')
rand=random.randint(0,6)
#TOSS
h_t_choice = ["Heads", "Tails"]
user_choice = input("Choose Heads or Tails.....")
c_choice = ["Bat", "Bowl"]
comp_choice = random.choice(h_t_choice)
print(f"{comp_choice}")
if user_choice == comp_choice:
    print("Hurray You have won the toss you choose bat or bowl")
    bat_bowl_choice=input("What would you like to choose Bat or Bowl")
    #Player won toss choose to bat
    if bat_bowl_choice == "Bat":
        balls=12
        ballsb=0
        p_runs=0
        print("!!!!!!!!!Lets play!!!!!!!!!!!\n")
        while ballsb < balls:
            runs=int(input("Enter runs to bat"))
            comp_bowl_choice=random.randint(0,6)
            if runs==comp_bowl_choice:
                print(f"You choose {runs},computer's choice is {comp_bowl_choice}")
                print(f"You are Out.Your total score is {p_runs} \n")
                break
            elif runs>6:
                print("Invalid Input enter a number below 7")
                continue
            else:
                p_runs += runs
                print(f"Runs scored: {runs}, Computer choice : {comp_bowl_choice}")
                print(f"Total runs scored {p_runs}\n")
            ballsb += 1
            #Computer Batting 2nd Innings
        print("Computer Batting...........\n")
        balls2 = 12
        ballsb2 = 0
        co_runs = 0
        print("!!!!!!!!!play!!!!!!!!!!!\n")
        while ballsb2 < balls2:
            bowl = int(input("Enter input from 1 to 6"))
            comp_bat_choice = random.randint(0, 6)
            if bowl== comp_bat_choice:
                print(f"You choose {bowl},computer's choice is {comp_bat_choice}")
                print(f"Total score is {co_runs} \n")
                break
            elif bowl > 6:
                print("Invalid Input enter a number below 7")
                continue
            else:
                co_runs += bowl
                print(f"Input: {bowl}, Computer choice : {comp_bat_choice}")
                print(f"Total runs scored {p_runs}\n")
            ballsb2 += 1
            ## RESULTS
    print("-----------------------------------\nRESULTS: ")
    if co_runs < p_runs:
        print(f"\nYou have wow the game. \n\nYour total runs are {p_runs} in {ballsb} balls and the computer scored {co_runs} in {ballsb2} bowls")
    elif co_runs == p_runs:
        print(f"The game is a tie, You score {p_runs} and the computer also scored {co_runs}")
    else:
        print(f"\nComputer won the game.\n\nComputer's total runs are {co_runs} in {ballsb2} bowls, and you score {p_runs}")
#Player won toss choose to bowl
#1st Innings
    if bat_bowl_choice == "Bowl":
        print("!!!!!!!!\nComputer batting\n")
        balls3 = 12
        ballsb3 = 0
        co_runs2 = 0
        while ballsb3 < balls3:
            bowls = int(input("Enter runs to bowl: "))
            comp_bat_choice2 = random.randint(1, 10)
            if comp_bat_choice2 == bowls:
                print(f"Computer's number is {comp_bat_choice2}, Your number is {bowls}")
                print(f"Total runs are {co_runs2}")
                break
            else:
                co_runs2 += comp_bat_choice2
                print(f"Computer's number is {comp_bat_choice2}, Your number is {bowls}")
                print(f"Computer's score is {co_runs2}\n")
            ballsb3 += 1
        ## Player Batting
        ## 2ND Innings
        balls4 = 12
        ballsb4 = 0
        p_runs2 = 0
        print("!!!!!!\nYour batting\n")
        while ballsb4 < balls4:
            runs2 = int(input("Enter a number to bat: "))
            comp_bowl_choice2 = random.randint(1, 10)

            if runs2 == comp_bowl_choice2:
                print(f"Your number is {p_runs2}, Computer's number is {comp_bowl_choice2}")
                print(f"Total score is {runs2}\n")
                break
            elif runs2 > 10:
                print("Invalid Input enter a number below 7")
                continue
            else:
                p_runs2 += runs2
                print(f"Your number: {runs2}, Computer's number: {comp_bowl_choice2}")
                print(f"Total runs {p_runs2}\n")

                if p_runs2 > co_runs2:
                    break
                ballsb4 += 1
            print("!!!!!!\nRESULTS: ")
            if co_runs2 < p_runs2:
                print( f"\nYou have wown the game. \n\nYour total runs are {p_runs2} and Bowls taken(Out of 12) are {ballsb4}\n Computer's total runs are {co_runs2}")
            elif co_runs2 == p_runs2:
                print(f"The game is a tie, You score {p_runs2} and the computer also scored {co_runs2}")
            else:
                print(f"\nComputer won the game.\n\nComputer's total runs are {co_runs2} and in {ballsb3} balls and your runs are {p_runs2}")
elif user_choice != "Heads" or "Tails":
    print("Enter valid input heads or tails")
else:
    #Computer Batting 1st Innings
    balls3 = 12
    ballsb3 = 0
    co_runs2 = 0
    while ballsb3 < balls3:
        bowls = int(input("Enter runs to bowl: "))
        comp_bat_choice2 = random.randint(1, 10)
        if comp_bat_choice2 == bowls:
            print(f"Computer's number is {comp_bat_choice2}, Your number is {bowls}")
            print(f"Total runs are {co_runs2}")
            break
        else:
            co_runs2 += comp_bat_choice2
            print(f"Computer's number is {comp_bat_choice2}, Your number is {bowls}")
            print(f"Total score is {co_runs2}\n")
        ballsb3 += 1
    balls4 = 12
    ballsb4 = 0
    p_runs2 = 0
    print("!!!!!!\nYour batting\n")
    while ballsb4 < balls4:
        runs2 = int(input("Enter a number to bat: "))
        comp_bowl_choice2 = random.randint(1, 10)

        if runs2 == comp_bowl_choice2:
            print(f"Your number is {p_runs2}, Computer's number is {comp_bowl_choice2}")
            print(f"Total score is {runs2}\n")
            break
        elif runs2 > 10:
            print("Invalid Input enter a number below 7")
            continue
        else:
            p_runs2 += runs2
            print(f"Your number: {runs2}, Computer's number: {comp_bowl_choice2}")
            print(f"Runs {p_runs2}\n")

            if p_runs2 > co_runs2:
                break
            ballsb4 += 1
        print("!!!!!!\nRESULTS: ")
        if co_runs2 < p_runs2:
            print(
                f"\nYou have won the game. \n\nYour total runs are {p_runs2} and Bowls taken(Out of 12) are {ballsb4}\n Computer's total runs are {co_runs2}")
        elif co_runs2 == p_runs2:
            print(f"The game is a tie, You score {p_runs2} and the computer also scored {co_runs2}")
        else:
            print(f"\nComputer won the game.\n\nComputer's total runs are {co_runs2} and in {ballsb3} balls and your runs are {p_runs2}")
input("Press any key to exit")