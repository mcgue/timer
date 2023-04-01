# Countdown timer

import time

# Function to do countdown
def countdown(length):
  # Convert length to integer
  length = int(length)
  # Loop to countdown to 0
  while length:
    # Get minutes and seconds
    mins, secs = divmod(length, 60)
    timer = f'{mins}:{secs}'
    print(timer)
    length -= 1
  print ('Zero')

# Get user input on length of timer
length = input('How many seconds do you want to count down from? ')
countdown(length)




