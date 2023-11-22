def main():
    stack = []
    while True:
        try:
            allowed_commands = ['PUSH', 'POP', 'SWAP', 'DUP', 'SWITCH', '+', '-', '*', '/']
            
            # User inputs
            user_input = input("Enter a command: ")

            if user_input.startswith('PUSH'):
                if len(user_input.split()) == 2:
                    _, num = user_input.split()
                    if num.isdigit():
                        stack.append(int(num))
                        print(f'stack is {stack}')
                    else:
                        print(f'invalid input, please enter an integer')
                else:
                    print(f'invalid input, please enter PUSH followed by a number')

            elif user_input in allowed_commands:
                # todo add process
                print(f"stack is {stack}")
            else:
                print("Invalid Input. Please enter a valid command. 'PUSH', 'POP', 'SWAP', 'DUP', '+', '-', '*' OR '/'")

            print(f"{user_input}")

        except Exception as e:
            # Handle additional exceptions
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
