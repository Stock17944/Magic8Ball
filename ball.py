import time, sys
from random import randint
responses = []
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
