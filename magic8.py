# Import random package into our program
import random

# Define flow needed variables
name = ""
question = "Will I be rich?"
answer = ""

# Generates a random number between 1 (inclusive) and 9 (inclusive)
random_number = random.randint(1, 9)

#print("The number generated is", random_number)

# Defines the answer based on the randomly generated number.
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:  
  answer ="Better not tell you now"
elif random_number == 7:  
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

#Printing logic with or without name fill
if name != "" and question != "":
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)
else:
  print("Question:", question)
  print("Magic 8-Ball's answer:", answer)
