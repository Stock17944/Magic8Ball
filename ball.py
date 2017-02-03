import time
from random import randint
responses = []
with open('responses.txt', 'r') as f:       
   for line in f:
      response = str(line)
      responses.append(response)  
rnumber = len(responses)
input("What is your question?")
rn = randint(1,rnumber)
print(responses[rn])
