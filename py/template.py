
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
    try:
        # Check if the inputs are positive integers
        if num <= 0 or den <= 0:
            raise ValueError("Both numerator and denominator must be positive integers.")

        # Calculating GCD for the numerator and denominator
        common_divisor = gcd(num, den)

        # Reducing the fraction
        reduced_numerator = num // common_divisor
        reduced_denominator = den // common_divisor

        return reduced_numerator, reduced_denominator

    except TypeError:
        # Handle the case where the inputs are not integers
        raise TypeError("Numerator and denominator must be integers.")

    except ZeroDivisionError:
        # Handle division by zero
        raise ZeroDivisionError("Denominator cannot be zero.")

# Example usage
exercise1(8, 12)  # This should return (2, 3) as 8/12 reduces to 2/3


# Exercise 2 - Magical Dates
def exercise2(day,month,year):
    return None

# Exercise 3 - All Sublists
def exercise3(l):
    return None

# Exercise 4 - English to Pig Latin Translator
def exercise4(word):
    return None

# Exercise 5 - Morse Code Encoder
def exercise5(message):
    return None

# Exercise 6 - Spelling Out Numbers
def exercise6(num):
    return None

# Exercise 7 - No Functions without Comments
def exercise7(filename):
    return None

# Exercise 8 - Justify any Text
def exercise8(filename,length):
    return None

# Exercise 9 - Knight's Challenge
def exercise9(start,end,moves):
    return None

# Exercise 10 - War of Species
def exercise10(environment):
    return None
