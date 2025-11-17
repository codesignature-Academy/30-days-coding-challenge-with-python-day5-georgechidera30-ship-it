while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Exiting program...")
        break

    # Try converting input to a number
    try:
        number = float(user_input)

        # Check if number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")