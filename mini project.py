def audit_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if score == 4:
        return "STRONG "
    elif score == 3:
        return "MEDIUM "
    elif score == 2:
        return "LITTLE WEAK"
    else:
        return "WEAK "
passwords_to_test = input("Enter passwords to audit: ").split(",")
print("--- PASSWORD SECURITY AUDIT ---")
print(f"{'PASSWORD':<15} | {'STRENGTH'}")
print("-" * 30)

for p in passwords_to_test:
    grade = audit_password(p)
    print(f"{p:<15} | {grade}")