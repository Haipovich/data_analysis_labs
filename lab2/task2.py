num_passwords = int(input())

UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER = set("abcdefghijklmnopqrstuvwxyz")
DIGITS = set("0123456789")
SPECIAL = set("!@#$%&*+")

for _ in range(num_passwords):
    password = str(input())
    if len(password) < 12:
        print("Invalid")
        continue

    has_upper = has_lower = has_digit = has_special = False

    for char in password:
        if char in UPPER:
            has_upper = True
        elif char in LOWER:
            has_lower = True
        elif char in DIGITS:
            has_digit = True
        elif char in SPECIAL:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Valid")
    else:
        print("Invalid")
