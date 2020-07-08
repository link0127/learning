
"""

sys¶
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

Documentation

In [ ]:
# sys example
import os
import sys

# this command is more simple and understandable if run in a separate argv.py file for example.
print(sys.argv)
# print as many '*' as our terminal width is (not working quite well in jupyter)
print("*" * os.get_terminal_size()[0])
print(f"We are running on {sys.platform}")
print("*" * os.get_terminal_size()[0])
# Exit program with error code 1
sys.exit(1)

"""

"""
Write a function named circle(radius, char="*") which returns an ascii circle with
the specified radius and char character.

Output will look weird because the terminal is using characters where height is not the same as width.
So it will look rather an ellipse. Bonus if you draw more realistic circle than me: :)

sample output:
circle(10, '#')
        #####
      #       #
    #           #
   #             #
  #               #

 #                 #

#                   #
#                   #
#                   #
#                   #
#                   #

 #                 #

  #               #
   #             #
    #           #
      #       #
        #####

# Beginner python - Lesson 4 - homework 4
# ASCII circle
# level: medium
# Hint: use math module
"""

import math

def circle(radius, char="*"):

    DrawCircle = (math.radians(radius))

    return DrawCircle

print(circle(16, '#'))

a = math.radians(radius)

print(a)