def password_quality_checker(password):
    """
    Check the quality of a password based on certain criteria.

    Parameters:
    password (str): The password to be checked.

    Returns:
    str: A message indicating the quality of the password.
    """

    # Criteria for a strong password
    MIN_LENGTH = 8
    MIN_UPPERCASE = 1
    MIN_LOWERCASE = 1
    MIN_DIGITS = 1
    MIN_SPECIAL_CHARS = 1

    # Check password length
    if len(password) < MIN_LENGTH:
        return "Password is too short. It should be at least {} characters long.".format(MIN_LENGTH)

    # Check for uppercase letters
    if sum(1 for char in password if char.isupper()) < MIN_UPPERCASE:
        return "Password should contain at least {} uppercase letter(s).".format(MIN_UPPERCASE)

    # Check for lowercase letters
    if sum(1 for char in password if char.islower()) < MIN_LOWERCASE:
        return "Password should contain at least {} lowercase letter(s).".format(MIN_LOWERCASE)

    # Check for digits
    if sum(1 for char in password if char.isdigit()) < MIN_DIGITS:
        return "Password should contain at least {} digit(s).".format(MIN_DIGITS)

    # Check for special characters
    special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    if sum(1 for char in password if char in special_chars) < MIN_SPECIAL_CHARS:
        return "Password should contain at least {} special character(s) from the following: {}".format(
            MIN_SPECIAL_CHARS, special_chars)

    return "Password is strong."


# Test the function
password = input("Enter a password: ")
result = password_quality_checker(password)
print(result)
