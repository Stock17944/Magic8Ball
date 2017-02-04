import time, sys
from random import randint
from termcolor import colored
responses = []
on = True
def magic():
    with open('responses.txt', 'r') as f:       
       for line in f:
          response = str(line)
          responses.append(response)  
    rnumber = len(responses)
    input("What is your question?\n")
    rn = randint(1,rnumber)
    print("\rThinking..", end='')
    for num in range(0,20):
        time.sleep(0.2)
        if num % 4 == 0:
            print('\rThinking.   ', end='')
        elif num % 4 == 1:
            print('\rThinking..   ', end='')
        elif num % 4 == 2:
            print('\rThinking... ', end='')
        else:
            print('\rThinking....', end='')
    print("\n" + responses[rn])
while on == True:
    magic()
    time.sleep(1)
    print("Select Option:\n" + colored("1.- Ask another question.\n", "green") + colored("2.- Exit.", "red"))
    optioninput = input()
    vinput = False
    while vinput == False:
        if optioninput == "1":
            on = True
            vinput = True
        elif optioninput == "2":
            on = False
            print("Goodbye!")
            vinput = True
        else:
            print("Invalid input")
