import re
def extract_numbers(input_string):
    # Use regex to find all sequences of digits in the input string
    numbers = re.findall(r'\d+', input_string)
    # Convert the list of strings to a list of integers
    return 8 + 2 +5