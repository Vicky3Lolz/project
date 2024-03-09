print("Welcome to my 4 function calculator :)")

while True:
    selection = input("Select an operation: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division (Enter in a number.): ")
    if selection in ("1","2","3","4"):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if selection == "1":
                print(a, "+", b, "=", a + b)
        elif selection == "2":
                print(a, "-", b, "=", a - b)
        elif selection == "3":
                print(a, "*", b, "=", a * b)
        elif selection == "4":
                print(a, "/", b, "=", a / b)

        choice = input("Use calculator again? (yes/no)")
        if choice == "no":
            break
        elif choice == "yes":
              continue
        if choice not in ("yes", "no"):
              print("Invalid Input")

    if selection not in ("1", "2", "3", "4"):
      print("Invalid input, please try again.")
          
        