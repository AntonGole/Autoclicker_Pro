from random import *


# Calculate a random delay from minutes, seconds and milliseconds
def random_delay(minutes, seconds, millis):
    totalMs = minutes * 60000 + seconds * 1000 + millis
    return randint(0, totalMs)


# Calculate the next delay using the random_delay function and the staticDelay variable
def calculate_new_delay(staticDelay, tfList):
    return ((staticDelay + random_delay(int(tfList[3].get()),
                                        int(tfList[4].get()),
                                        int(tfList[5].get())) - 11) / 1000)


# Calculate the next double click delay using randint
def calculate_new_doubleclick_delay():
    return randint(128, 315) / 1000
