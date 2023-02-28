# Use this code with: https://github.com/Epic4773/Learning-Python/blob/main/your-mom

import random

class Die:
  def __init__(self, sides):
    self.sides = sides
  
  def roll_die(self):
    print(random.randint(1, self.sides))
