# Import the 're' library for regular expression operations
import re

# Function to assess the strength of a given password
def assess_password_strength(password):
    """
    Analyzes the strength of a password based on multiple criteria:
    1. Minimum length of 8 characters
    2. Contains at least one uppercase letter
    3. Contains at least one lowercase letter
    4. Contains at least one numeric digit
    5. Contains at least one special character
    
    Args:
        password (str): The password to assess.
    
    Returns:
        None: Prints the analysis and strength of the password.
    """
    # Criteria checks using regular expressions
    length = len(password) >= 8  # Check if the password has at least 8 characters
    has_uppercase = bool(re.search(r"[A-Z]", password))  # Check for uppercase letters
    has_lowercase = bool(re.search(r"[a-z]", password))  # Check for lowercase letters
    has_numbers = bool(re.search(r"[0-9]", password))    # Check for numeric digits
    has_special_char = bool(re.search(r"[!@#$%^&*()_+=\-{}[\]|:;\"'<>,.?/]", password))  # Check for special characters
    
    # Calculate the total score based on the criteria met
    score = sum([length, has_uppercase, has_lowercase, has_numbers, has_special_char])
    
    # Provide feedback on the password's strengths and weaknesses
    print("Password Assessment:")
    
    if length:
        print("- Good length (8+ characters)")
    else:
        print("- Password should be at least 8 characters long")
        
    if has_uppercase:
        print("- Contains uppercase letters")
    else:
        print("- Add uppercase letters for stronger security")
    
    if has_lowercase:
        print("- Contains lowercase letters")
    else:
        print("- Add lowercase letters for stronger security")
        
    if has_numbers:
        print("- Contains numbers")
    else:
        print("- Add numbers for stronger security")
        
    if has_special_char:
        print("- Contains special characters")
    else:
        print("- Add special characters for stronger security")

    # Assess the overall strength based on the score
    if score == 5:
        print("Strength: Very Strong")
    elif score == 4:
        print("Strength: Strong")
    elif score == 3:
        print("Strength: Moderate")
    elif score == 2:
        print("Strength: Weak")
    else:
        print("Strength: Very Weak")

# Prompt the user to enter a password for strength assessment
password = input("Enter your password to assess its strength: ")

# Call the function to analyze the password
assess_password_strength(password)
