def is_palindrome(s):
    """
    Check if a given string is a palindrome.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the cleaned string to its reverse
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    # Example strings to check
    examples = [
        "A man, a plan, a canal, Panama!",
        "No lemon, no melon",
        "Hello, World!",
        "racecar"
    ]

    for example in examples:
        result = is_palindrome(example)
        print(f"'{example}' is a palindrome: {result}")
