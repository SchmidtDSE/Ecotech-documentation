"""
Will the potato explode in the microwave? Today, we find out.
"""

# TODO: This code is very badly documented! Please help to clean it up so that we can properly test our potatoes.

def one(potato):
    """
    # ¯\_(ツ)_/¯ Good luck, future developer.
    """
    if potato['weight'] < 0.3:
        return "Small"
    elif (potato['weight'] >= 0.3 & potato['weight'] < 0.6):
        return "Medium"
    else:
        return "A Chonker" # i wonder what shape this potato is

# how long to microwave the potato
def beep_boop_vrrrr(x):
    if x < 1:
        return "short"
    elif (x >= 11 & x < 3):
        return "medium"
    elif (x >= 3 & x < 5):
        return "long"
    
# another function
def something(holes):
    if holes == 'yes': # what did we poke the holes with?
        return True
    else:
        return False
    
# i hope this code runs
def boom(potato):
    if one(potato) == "Small":
        if beep_boop_vrrrr(potato['time']) == "short" or beep_boop_vrrrr(potato['time']) == "medium":
            return "Boooo. Boring."
        else:
            if something(potato['holes']):
                return "I wonder if it will be tasty."
            else:
                return "Today, we test the limits of this tiny potato."
    elif one(potato) == "Medium":
        if beep_boop_vrrrr(potato['time']) == "short":
            return "Boooo. Boring."
        elif beep_boop_vrrrr(potato['time']) == "medium":
            return "Hmmmmm. Interesting."
        else:
            return "A science experiment in the making!"
    # a chonker
    else:
        if beep_boop_vrrrr(potato['time']) == "short":
            return "Boooo. Boring."
        elif beep_boop_vrrrr(potato['time']) == "medium":
            return "You only live once. Microwave it."
        else:
            return "Boom boom pow pow! Might need a new microwave."
