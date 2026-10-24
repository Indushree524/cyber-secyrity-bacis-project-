
import string


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if len(password) < 8:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score


def main():
    password = input("Enter a password to check: ")
    strength, score = check_password_strength(password)

    print("Password strength:", strength)
    print("Score:", score, "/ 5")


if __name__ == "__main__":
    main()
