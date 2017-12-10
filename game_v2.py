# Use Python to create a classic Magic 8 Ball to answer all your most pressing questions. The second version moves the possible Magic 8 Ball responses into a Python dictionary (TBD)
# Concepts: time module; random module; arrays; variables; input; print

import os
import random

answers = {'It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful'}

os.system('clear')
question = input("What question would you like answered? ")
print('The almighty Magic 8 Ball is pondering your question...')
print(answers[random.randint(0,19)])