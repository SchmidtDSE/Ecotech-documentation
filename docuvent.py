

# TODO: This code is very badly documented! Please help to clean it up so that we can properly test our potatoes.
# You do not need to run the code.

def one(weight):
    """
    # ¯\_(ツ)_/¯ Good luck, future developer.
    """
    if weight < 0.3:
        return "Small"
    elif (weight >= 0.3 & weight < 0.6):
        return "Medium"
    else:
        return "A Chonker" # i wonder what shape this potato is

# minutes
def beep_boop_vrrrr(x):
    if x < 1:
        return "short"
    elif (x >= 11 & x < 3):
        return "medium"
    elif (x >= 3 & x < 5):
        return "long"
    else:
        return "very long"
    
# another function
def something(holes_ithink):
    if holes_ithink == 'yes': # what did we poke the holes with?
        return True
    else:
        return False
    
# i hope this code runs
def boom(potato):
    if one(potato['weight']) == "Small":
        if beep_boop_vrrrr(potato['time']) == "short" or beep_boop_vrrrr(potato['time']) == "medium":
            return "Boooo. Boring."
        else:
            if something(potato['holes']):
                return "I wonder if it will be tasty."
            else:
                return "Today, we test the limits of this tiny potato."
    elif one(potato['weight']) == "Medium":
        if beep_boop_vrrrr(potato['time']) == "short":
            return "Boooo. Boring."
        elif beep_boop_vrrrr(potato['time']) == "medium":
            if something(potato['holes']):
                return "Hmmmmm. Interesting."
            else:
                return "I wonder if it will be tasty."
        else:
            return "A science experiment in the making!"
    # a chonker
    else:
        if beep_boop_vrrrr(potato['time']) == "short":
            return "Boooo. Boring."
        elif beep_boop_vrrrr(potato['time']) == "medium":
            if something(potato['holes']):
                return "Hmmmmm. Interesting."
            else: 
                return "You only live once."
        else:
            return "Boom boom pow pow! Might need a new microwave."
