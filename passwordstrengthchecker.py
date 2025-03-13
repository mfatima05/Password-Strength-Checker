import re

# Extended list of common passwords to avoid
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "abc123", "password1", "12345", 
    "1234", "12345678", "123", "Aa123456", "1234567890", "UNKNOWN", "1234567", 
    "123123", "111111", "Password", "12345678910", "000000", "Admin123", 
    "********", "admin", "user"
]

# Function to check password length
def check_length(password):
    return len(password) >= 8

# Function to check password complexity
def check_complexity(password):
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    return has_upper and has_lower and has_digit and has_special

# Function to check password uniqueness
def check_uniqueness(password):
    return password.lower() not in (pwd.lower() for pwd in COMMON_PASSWORDS)

# Function to validate the password and provide feedback
def validate_password(password):
    feedback = []
    if not check_length(password):
        feedback.append("❌ Password is too short. Use at least 8 characters.")
    if not check_complexity(password):
        feedback.append("❌ Password should include uppercase, lowercase, numbers, and special characters.")
    if not check_uniqueness(password):
        feedback.append("❌ Password is too common. Try a more unique password.")
    
    if not feedback:
        return "✅ Password is valid and strong!"
    else:
        return "\n".join(feedback)

# Main program
if __name__ == "__main__":
    password = input("Enter a password to check if it's valid: ")
    print("\nChecking password...")
    result = validate_password(password)
    print("\nResult:")
    print(result)
