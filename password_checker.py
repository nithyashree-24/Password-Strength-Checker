import re
import secrets
import string

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "letmein"
}

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add a special character.")

    if password.lower() in COMMON_PASSWORDS:
        score = max(0, score - 30)
        feedback.append("Avoid common passwords.")

    if re.search(r"(.)\1\1", password):
        score = max(0, score - 10)
        feedback.append("Avoid repeating the same character.")

    if score < 40:
        strength = "WEAK"
    elif score < 70:
        strength = "MEDIUM"
    elif score < 90:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return score, strength, feedback

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = "".join(secrets.choice(characters) for _ in range(length))

        if (
            re.search(r"[A-Z]", password)
            and re.search(r"[a-z]", password)
            and re.search(r"\d", password)
            and re.search(r"[^A-Za-z0-9]", password)
        ):
            return password

print("=" * 45)
print("       PASSWORD SECURITY ANALYZER")
print("=" * 45)

password = input("\nEnter your password: ")

score, strength, feedback = analyze_password(password)

print("\nSecurity Score:", score, "/ 100")
print("Strength:", strength)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
else:
    print("\nExcellent! Your password meets all checks.")

print("\nGenerated Secure Password:")
print(generate_password())

print("\nNote: Passwords are processed locally and are not stored.")
