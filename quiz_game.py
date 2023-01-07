print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Brain of computer is? ")
if answer.lower() == "cpu":
  print('Correct!')
  score += 1
else:
    print("Incorrect!")

answer = input("Who invented computer? ")
if answer.lower() == "charles babbage":
  print('Correct!')
  score += 1
else:
    print("Incorrect!")

answer = input("Which is the most sensitive organ in our body? ")
if answer.lower() == "skin":
  print('Correct!')
  score += 1
else:
    print("Incorrect!")

answer = input("Who is the Father of our Nation? ")
if answer.lower() == "mahatma gandhi":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

print("You got "  + str(score) +  " questions correct!")
print("You got "  + str((score / 4) * 100) +  "%.")