# Countdown timer
# Finished

# Import necessary module
import time

# Function to do countdown
def countdown(length):
  # Convert length to integer
  length = int(length)
  # Loop to countdown to 0
  while length:
    # print countdown
    print(length, end=" ")
    # Delay 1 second
    time.sleep(1)
    # Take off a second
    length -= 1

  # Print ending message
  print ('Done!')

# Get user input on length of timer
length = input('How many seconds do you want to count down from? ')

# Run Countdown timer
countdown(length)




