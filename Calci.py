import math

def show_menu():
    print("\n" + "="*35)
    print("      SCIENTIFIC CALCULATOR      ")
    print("="*35)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tangent (tan)")
    print("8. Degrees to Radians")
    print("9. Radians to Degrees")
    print("10. Square Root (√)")
    print("11. Power (x^y)")
    print("12. Print Pi (π)")
    print("13. Exit")
    print("="*35)

def get_input(prompt, is_float=True):
    while True:
        try:
            val = input(prompt)
            if val.lower() == 'pi':
                return math.pi
            return float(val) if is_float else int(val)
        except ValueError:
            print("Invalid input.")

def calculator():
    while True:
        show_menu()
        choice = get_input("\nChoose an option (1-13): ", is_float=False)

        if choice == 13:
            print("\nExiting calculator.")
            break

        if choice in [1, 2, 3, 4, 11]:
            num1 = get_input("Enter first number (or 'pi'): ")
            num2 = get_input("Enter second number (or 'pi'): ")

            if choice == 1:
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Error:Can't divide by zero")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif choice == 11:
                print(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")

        elif choice in [5, 6, 7, 8, 9, 10]:
            num = get_input("Enter the number/angle (or 'pi'): ")

            if choice == 5:
                
                print(f"Result: sin({num}) = {math.sin(num)}")
            elif choice == 6:
                print(f"Result: cos({num}) = {math.cos(num)}")
            elif choice == 7:
                if math.cos(num) == 0:
                    print("Error: Tangent is undefined for this angle.")
                else:
                    print(f"Result: tan({num}) = {math.tan(num)}")
            elif choice == 8:
                print(f"Result: {num}° = {math.radians(num)} radians")
            elif choice == 9:
                print(f"Result: {num} rad = {math.degrees(num)}°")
            elif choice == 10:
                if num < 0:
                    print("Error: Cannot calculate square root of a negative number in real domain.")
                else:
                    print(f"Result: √{num} = {math.sqrt(num)}")

        elif choice == 12:
            print(f"Value of Pi (π): {math.pi}")
        else:
            print("Invalid choice. Please select a number between 1 and 13.")

if __name__ == "__main__":
    calculator()