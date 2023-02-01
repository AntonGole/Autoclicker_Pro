from random import *
import scipy.stats


# Calculate a random delay from minutes, seconds and milliseconds
def random_delay(minutes, seconds, millis):
    totalMs = minutes * 60000 + seconds * 1000 + millis
    return randint(0, totalMs)


# Calculate a random delay from minutes, seconds and milliseconds using standard distribution
def random_delay_normal(minutes, seconds, millis):

    # Calculate maximus possible delay
    totalMs = minutes * 60000 + seconds * 1000 + millis
    print(totalMs)

    # Set variables for the normal distribution

    # Lower bound
    lower = 0

    # Upper bound
    upper = totalMs

    # Mean value
    mu = totalMs/2

    # Standard deviation
    sigma = totalMs/8

    # Sample one random number using normal distribution and the input variables declared above
    number = scipy.stats.truncnorm.rvs(
        (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=1)

    return randint(0, round(number[0]))


# Calculate the next delay using the random_delay function and the staticDelay variable
def calculate_new_delay(staticDelay, tfList):
    return ((staticDelay + random_delay_normal(int(tfList[3].get()),
                                        int(tfList[4].get()),
                                        int(tfList[5].get())) - 11) / 1000)


# Calculate the next double click delay using randint
def calculate_new_doubleclick_delay():
    return randint(128, 315) / 1000
