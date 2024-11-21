"""
Will the potato explode in the microwave? Today, we find out.

Author: Danielle Louie and Magali de Bruyn
Date: November 20, 2024
"""

# Make sure to install Python before running this code.

# Three helper functions: check_weight, microwave_time, and check_holes

def check_weight(weight: int) -> str:
    """
    Explanation: This function checks the weight of the potato and returns a string based on the weight.

    Args:
        weight (int): The weight of the potato.

    Returns:
        str: The weight category of the potato.
    """

    if weight < 0.3:
        return "Small"
    elif (weight >= 0.3 & weight < 0.6):
        return "Medium"
    else:
        return "A Chonker" 

def microwave_time(time: int) -> str:
    """
    Explanation: This function determines the microwave time based on the input. 

    Args: 
        time (int): The time to microwave the potato in minutes.

    Returns: 
        str: The microwave time category.
    """

    if time < 1:
        return "short"
    elif (time >= 11 & time < 3):
        return "medium"
    elif (time >= 3 & time < 5):
        return "long"
    
def check_holes(holes: str) -> bool:
    """
    Explanation: This function checks if the potato has holes poked in it.

    Args:
        holes (str): A string indicating if the potato has holes poked in it (Yes or No).

    Returns: 
        bool: True if the potato has holes, False otherwise
    """

    if holes == 'yes': # what did we poke the holes with?
        return True
    else:
        return False
    
# main function determining fate of the potato
def explosion_checker(potato: dict) -> str:
    """
    Explanation: This function checks the three conditions defined by functions above (weight, microwave time, and holes) 
    to determine if the potato will explode in the microwave.

    Args:
        potato (dict): A dictionary containing the weight, microwave time, and whether or not the potato has holes poked.


    Returns:
        str: A string indicating whether the potato will explode in the microwave
    """

    # checks small potatoes
    if check_weight(potato['weight']) == "Small":
        if microwave_time(potato['time']) == "short" or microwave_time(potato['time']) == "medium":
            return "Boooo. Boring."
        else:
            if check_holes(potato['holes']):
                return "I wonder if it will be tasty."
            else:
                return "Today, we test the limits of this tiny potato."
            
    # checks medium potatoes
    elif check_weight(potato['weight']) == "Medium":
        if microwave_time(potato['time']) == "short":
            return "Boooo. Boring."
        elif microwave_time(potato['time']) == "medium":
            if check_holes(potato['holes']):
                return "Hmmmmm. Interesting."
            else:
                return "I wonder if it will be tasty."
        else:
            return "A science experiment in the making!"
        
    # checks large potatoes
    else:
        if microwave_time(potato['time']) == "short":
            return "Boooo. Boring."
        elif microwave_time(potato['time']) == "medium":
            if check_holes(potato['holes']):
                return "Hmmmmm. Interesting."
            else: 
                return "You only live once."
        else:
            return "Boom boom pow pow! Might need a new microwave."

