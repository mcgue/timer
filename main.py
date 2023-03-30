# Countdown timer

import time

# Function to do countdown
def countdown(length):
  length = int(length)
  # Get minutes and seconds
  mins, secs = divmod(length, 60)
  timer = f'{mins}:{secs}'
  print(timer)

# Get user input on length of timer
length = input('How many seconds do you want to count down from? ')
countdown(length)




