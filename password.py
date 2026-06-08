import re

def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check digits
    if re.search(r"[0-9]", password):
        strength += 1

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1

    # Determine strength
    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Medium"
    else:
        return "Strong"


# Get password from user
password = input("Enter password: ")

# Check and display strength
result = check_password_strength(password)
print("Strength:", result)