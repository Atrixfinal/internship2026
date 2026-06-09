# 1.1. 
num = float(input("Enter a number: "))
if num >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# 1.2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 1.3
check_num = int(input("Enter an integer: "))
if check_num % 2 == 0:
    print(f"{check_num} is even.")
else:
    print(f"{check_num} is odd.")

# 2.1
marks = float(input("Enter your marks: "))
age = int(input("Enter your age: "))

if marks >= 60:
    if 17 <= age <= 25:
        print("Admission Approved.")
    else:
        print("Admission Denied: Age criteria not met.")
else:
    print("Admission Denied: Marks criteria not met.")

# 2.2
account_balance = 5000
withdrawal_amount = float(input("Enter amount to withdraw: "))

if withdrawal_amount <= account_balance:
    if withdrawal_amount % 100 == 0:
        account_balance -= withdrawal_amount
        print(f"Withdrawal successful! Remaining balance: ${account_balance}")
    else:
        print("Error: Please enter an amount in multiples of 100.")
else:
    print("Error: Insufficient balance.")

# 2.3
years_of_service = int(input("Enter years of service: "))
performance_rating = input("Enter performance rating (Excellent/Good/Poor): ").strip().capitalize()

if years_of_service >= 2:
    if performance_rating == "Excellent":
        print("Eligible for a 20% bonus.")
    elif performance_rating == "Good":
        print("Eligible for a 10% bonus.")
    else:
        print("Not eligible for a bonus due to rating.")
else:
    print("Not eligible for a bonus: Must complete at least 2 years of service.")

# 3.1
student_marks = float(input("Enter student marks: "))
if student_marks >= 90:
    print("Grade: A+")
elif student_marks >= 75:
    print("Grade: A")
elif student_marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

# 3.2
signal = input("Enter traffic light color (Red/Yellow/Green): ").strip().capitalize()
if signal == "Red":
    print("Stop!")
elif signal == "Yellow":
    print("Slow down/Prepare to stop.")
elif signal == "Green":
    print("Go!")
else:
    print("Invalid color entered.")

# 3.3
temp = float(input("Enter the temperature in Celsius: "))
if temp > 30:
    print("It's hot outside. Wear light clothes and stay hydrated!")
elif temp >= 15:
    print("The weather is pleasant. A t-shirt or light jacket will do.")
else:
    print("It's chilly! Wear a warm coat or sweater.")

# 4.1
stored_user = "admin"
stored_pass = "secure123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_user and password == stored_pass:
    print("Access Granted.")
else:
    print("Access Denied: Invalid credentials.")

# 4.2
has_good_credit = input("Do you have good credit? (yes/no): ").strip().lower() == "yes"
has_high_income = input("Do you have a high income? (yes/no): ").strip().lower() == "yes"

if has_good_credit and has_high_income:
    print("Loan Approved.")
elif has_good_credit or has_high_income:
    print("Loan Approved with conditions/co-signer required.")
else:
    print("Loan Rejected.")

# 4.3
gpa = float(input("Enter your GPA: "))
is_varsity_athlete = input("Are you a varsity athlete? (yes/no): ").strip().lower() == "yes"

if gpa >= 3.8 or (gpa >= 3.2 and is_varsity_athlete):
    print("Congratulations! You qualify for the scholarship.")
else:
    print("You do not qualify for the scholarship at this time.")

    # Subtask 1: Define Functions with Parameters
def greet_user(name):
    print(f"Hello, {name}!")



# Subtask 2: Return Values from Functions
def calculate_sum(a, b):
    return a + b

# Subtask 3: Use Default Parameters
def welcome_banner(name="Guest"):
    print(f"Welcome, {name}")

# Subtask 4: Understand Function Scope
global_var = 100  # Accessible anywhere

def scope_demonstration():
    local_var = 50  # Accessible only inside this function
    print(f"Inside function -> Global Variable: {global_var}")
    print(f"Inside function -> Local Variable: {local_var}")

# --- Demonstration of Functions ---
print("--- Function Demonstrations ---")
greet_user("Muni")

result = calculate_sum(10, 20)
print(f"Sum result: {result}")

welcome_banner()
welcome_banner("John")

scope_demonstration()

def calculate_grade():
    try:
        marks = float(input("Enter Marks: "))
        if marks < 0 or marks > 100:
            print("Invalid input. Marks should be between 0 and 100.")
            return

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "Fail"
            
        print(f"Grade: {grade}")
    except ValueError:
        print("Please enter a valid numeric value.")

calculate_grade()

def convert_celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter Temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.1f}°F")
    except ValueError:
        print("Please enter a valid numeric temperature.")

convert_celsius_to_fahrenheit()

def login_system():
    # Pre-stored registration database record
    db_username = "admin"
    db_password = "1234"
    
    print("--- Login Portal ---")
    user_input = input("Username: ")
    pass_input = input("Password: ")
    
    if user_input == db_username and pass_input == db_password:
        print("\nLogin Successful")
    else:
        print("\nLogin Failed: Incorrect username or password.")

login_system()

def factorial(n):
    if n < 0:
        return "Undefined (Factorial does not exist for negative numbers)"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Execution and UI display
try:
    num_input = int(input("Enter Number: "))
    fact_result = factorial(num_input)
    print(f"Factorial: {fact_result}")
except ValueError:
    print("Please enter a valid whole integer.")