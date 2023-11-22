def main():
    stack = []
    while True:
        try:
            allowed_commands = ['PUSH', 'POP', 'SWAP', 'DUP', 'SWITCH', '+', '-', '*', '/']
            
            # User inputs
            user_input = input("Enter a command: ")

            if user_input in allowed_commands:
                # todo add process
                process_command(user_input, stack)
                print(f"stack is {stack}")
            else:
                print("Invalid Input. Please enter a valid command. 'PUSH', 'POP', 'SWAP', 'DUP', '+', '-', '*' OR '/'")

            print(f"{user_input}")

        except Exception as e:
            # Handle additional exceptions
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
