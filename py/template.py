
# Exercise 1 - Smallest Fraction Terms
def exercise1(num: int,
              den: int) -> tuple:
    """
    Reduces a fraction to its lowest terms and returns the numerator and denominator.

    Parameters:
    numerator (int): The numerator of the fraction.
    denominator (int): The denominator of the fraction.

    Returns:
    (int, int): A tuple containing the numerator and denominator of the reduced fraction.
    """
    # Function to find the Greatest Common Divisor (GCD)
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    # Check if the inputs are positive integers
    if num <= 0 or den <= 0:
        raise ValueError("Both numerator and denominator must be positive integers.")
    else:
        # Calculating GCD for the numerator and denominator
        divisor = gcd(num, den)

        # Reducing the fraction
        reduced_num = num // divisor
        reduced_den = den // divisor

        return reduced_num, reduced_den

# Exercise 2 - Magical Dates
def exercise2(day: int, 
              month: int,
              year: int) -> bool:
    """
    Check if a given date is a magic date.
    A magic date occurs when the day multiplied by the month equals the last two digits of the year.

    Parameters:
    day (int): The day of the date.
    month (int): The month of the date.
    year (int): The year of the date.

    Returns:
    bool: True if the date is a magic date, False otherwise.
    """
    # Multiply day and month
    product = day * month

    # Get last two digits of the year
    last_two_digits = year % 100

    # Check if product equals the last two digits of the year
    return product == last_two_digits


# Exercise 3 - All Sublists
def exercise3(l: list) -> list:
    """
    Generate all possible sublists of a given list.

    Parameters:
    input_list (list): The list from which sublists are to be generated.

    Returns:
    list: A list of all possible sublists.
    """
    sublists = [[]]
    for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            # Slice the input list to get the sublist
            sublist = l[i:j]
            sublists.append(sublist)
    return sublists

# Exercise 4 - English to Pig Latin Translator
def exercise4(word: str) -> str:

    """
    Translate an English word to Pig Latin.

    Rules:
    - If the word begins with a consonant (including 'y'), move all letters before the first vowel to the end and add 'ay'.
    - If the word begins with a vowel (excluding 'y'), add 'way' to the end.
    - Handle uppercase letters and punctuation.

    Parameters:
    word (str): The English word to translate.

    Returns:
    str: The translated Pig Latin word.
    """
    # Check if the word is empty
    if not word:
        return word

    # Check for punctuation at the end
    punctuation = ''
    if word[-1] in ",.?!":
        punctuation = word[-1]
        word = word[:-1]

    # Find the first vowel in the word
    first_vowel_index = 0
    for i, letter in enumerate(word.lower()):
        if letter in 'aeiou':
            first_vowel_index = i
            break

    # Translate to Pig Latin
    if first_vowel_index == 0:
        translated_word = word + 'way'
    else:
        start = word[first_vowel_index:]
        end = word[:first_vowel_index] + 'ay'
        translated_word = start + end

    # Handle uppercase
    if word[0].isupper():
        translated_word = translated_word.capitalize()

    return translated_word + punctuation

# Exercise 5 - Morse Code Encoder
def exercise5(message: str) -> str:
    """
    Encode a string into Morse code.

    Parameters:
    message (str): The string of letters and numbers to encode.

    Returns:
    str: The Morse code representation of the input string.
    """
    # Morse code dictionary
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
        '0': '-----'
    }

    # Remove non-alphanumeric characters
    message = ''.join(filter(str.isalnum, message.upper()))

    # Encode the text into Morse code
    morse_code = ' '.join(morse_code_dict[char] for char in message if char in morse_code_dict)

    return morse_code


# Exercise 6 - Spelling Out Numbers
def exercise6(num: int) -> str:
    """
    Convert an integer to its English words representation.
    
    Parameters:
    num (int): The integer to convert, between 0 and 999 inclusive.
    
    Returns:
    str: The English words for the input number.
    """
    # Define dictionaries for number segments
    ones = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
             'seventeen', 'eighteen', 'nineteen')
    tens = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    
    # Initialize the result string
    words = ''
    
    # Handle hundreds
    if num >= 100:
        words += ones[num // 100] + ' hundred' if num // 100 > 1 else 'a hundred'
        num %= 100
        if num:
            words += ' and '
    
    # Handle tens and ones
    if num >= 20:
        words += tens[num // 10]
        num %= 10
        if num:
            words += '-' + ones[num]
    elif num >= 10:
        words += teens[num - 10]
    elif num > 0:
        words += ones[num]
    
    return words


# Exercise 7 - No Functions without Comments
def exercise7(filename: str) -> list[str]:
    """
    Identify functions in a Python source file that do not have preceding comments.
    
    Parameters:
    filename (str): The path to the source file to analyze.
    
    Returns:
    list: A list of function names without preceding comments.
    """
    # Initialize a list to hold the names of functions without comments
    functions_without_comments = []

    # Open the file and read the lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Iterate through the lines of the file
    for i, line in enumerate(lines):
        # Check if the line starts with 'def '
        if line.startswith('def '):
            # Extract the function name
            function_name = line.split('(')[0].replace('def ', '').strip()
            # Check if the previous line is a comment
            if i == 0 or not lines[i-1].strip().startswith('#'):
                functions_without_comments.append(function_name)

    return functions_without_comments


# Exercise 8 - Justify any Text
def exercise8(filename: str,
              length: int) -> list[str]:
    """
    Read lines from a file and split them into strings with a maximum length.
    
    Parameters:
    filename (str): The path to the file to read.
    max_length (int): The maximum allowed length for each line.
    
    Returns:
    list: A list of strings, each not exceeding the maximum length.
    """
    # Initialize a list to store the processed lines
    processed_lines = []

    # Open the file and read lines
    with open(filename, 'r') as file:
        words = file.read().split()

    # Temporary list to hold words for the current line
    current_line = []
    current_length = 0

    for word in words:
        # Check if adding the next word would exceed the max_length
        if current_length + len(word) + len(current_line) > length:
            # Join the current line and add it to the processed lines
            processed_lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            # Add the word to the current line
            current_line.append(word)
            current_length += len(word)

    # Add the last line if it's not empty
    if current_line:
        processed_lines.append(' '.join(current_line))

    return processed_lines


# Exercise 9 - Knight's Challenge
def exercise9(start: str, 
              end: str, 
              moves: int) -> bool:
    """
    Determine if a knight can reach the final position from the initial position in at most the given number of moves.

    Parameters:
    start (str): The initial position of the knight (e.g., 'a1').
    end (str): The final position to reach (e.g., 'c5').
    moves (int): The maximum number of moves allowed.

    Returns:
    bool: True if the knight can reach the final position within the given moves, False otherwise.
    """
    # Convert the position to (row, column)
    def pos_to_rc(pos):
        col, row = ord(pos[0]) - ord('a'), int(pos[1]) - 1
        return (row, col)

    # Calculate possible moves from a given position
    def get_knight_moves(pos):
        row, col = pos
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]

    # Recursive function to search for the final position
    def search(pos, final, moves_remaining):
        if moves_remaining < 0:
            return False
        if pos == final:
            return True
        for next_move in get_knight_moves(pos):
            if search(next_move, final, moves_remaining - 1):
                return True
        return False

    initial_rc = pos_to_rc(start)
    final_rc = pos_to_rc(end)
    return search(initial_rc, final_rc, moves)



# Exercise 10 - War of Species
def exercise10(environment: list[str]) -> list[str]:
    """
    Simulate the War of Species on a grid.

    Parameters:
    environment (list of str): The current state of the environment as a list of strings.

    Returns:
    list of str: The next state of the environment as a list of strings.
    """
    def count_neighbors(x, y):
        # Counts the number of each species around a given cell
        counts = {'X': 0, 'O': 0, '.': 0}
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                if 0 <= x + dx < len(environment) and 0 <= y + dy < len(environment[0]):
                    counts[environment[x + dx][y + dy]] += 1
        return counts
    
    def next_cell_state(x, y):
        # Determines the next state for a single cell
        neighbors = count_neighbors(x, y)
        cell = environment[x][y]
        total_neighbors = neighbors['X'] + neighbors['O']
        
        if cell == '.' and max(neighbors['X'], neighbors['O']) >= 2:
            return 'X' if neighbors['X'] > neighbors['O'] else 'O' if neighbors['O'] > neighbors['X'] else '.'
        elif cell != '.' and (total_neighbors > 6 or neighbors[cell] < 3 or neighbors['X' if cell == 'O' else 'O'] > neighbors[cell]):
            return '.'
        else:
            return cell
    
    # Create the next state of the environment
    next_grid = []
    for x in range(len(environment)):
        next_row = ''.join(next_cell_state(x, y) for y in range(len(environment[0])))
        next_grid.append(next_row)
    
    return next_grid
