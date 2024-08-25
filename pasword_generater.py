import random
import string
def generate_password(length=12, include_symbols=True):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if include_symbols else ''
    # Combine all character sets
    all_characters = lower + upper + digits + symbols

    # Ensure the password has at least one character from each set
    if include_symbols:
        if length < 4:
            raise ValueError("Password length should be at least 4 characters to include all character types.")
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols),
        ]
    else:
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
        ]
    # Fill the rest of the password length with random characters from all character sets
    password += random.choices(all_characters, k=length - len(password))
    # Shuffle the result to ensure randomness
    random.shuffle(password)
    # Convert list to string
    return ''.join(password)
def main():
    length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'  
    try:
        password = generate_password(length, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
