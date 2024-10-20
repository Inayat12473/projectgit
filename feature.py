 
def check_age(age):
    if age >= 18:
        return "You are eligible."
    else:
        return "You are not eligible."

# Input: User's age
age = int(input("Enter your age: "))

# Output: Age eligibility check
result = check_age(age)
print(result)