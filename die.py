# Use the following link to make a seperate file called "main.py": https://github.com/Epic4773/Learning-Python/blob/main/42.%20Die%20Class%20Assignment%20(Task%201)
import random

class Die:
  def __init__(self, sides):
    self.sides = sides
  
  def roll_die(self):
    print(random.randint(1, self.sides))
