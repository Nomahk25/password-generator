import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Characters to choose from
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensuring the password has at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle for randomness
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")
