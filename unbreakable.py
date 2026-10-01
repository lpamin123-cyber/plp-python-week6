# unbreakable.py
# Handles user input continuously without crashing on invalid inputs

def get_valid_number():
    while True:
        user_input = input("Enter a whole number: ")
        try:
            val = int(user_input)
            return val
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")

if __name__ == "__main__":
    print("Program running. Enter a number to test:")
    num = get_valid_number()
    print(f"You entered: {num}")
