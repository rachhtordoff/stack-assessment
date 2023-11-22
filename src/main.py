def main():
    stack = []
    while True:
        try:
            allowed_commands = ['PUSH', 'POP', 'SWAP', 'DUP', '+', '-', '*', '/']

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
                    print(f'Invalid input, please enter PUSH followed by a number: {user_input}')

            elif user_input in allowed_commands:
                process_command(user_input, stack)
                print(f"stack is {stack}")
            else:
                print("Invalid Input. Please enter a valid command. 'PUSH', 'POP', 'SWAP', 'DUP', '+', '-', '*' OR '/'")

            print(f"{user_input}")

        except KeyboardInterrupt:
            # handle user tryimg to exit
            print("\nExiting..")
            break
        except Exception as e:
            #handle additional exceptions
            print(f"Error: {e}")


def process_command(command, stack):
    #empty stack
    if command == 'POP' and stack:
        return stack.pop()

    #switch element places of the last 2 elements in list
    elif command == 'SWAP' and len(stack) > 1:
        stack[-1], stack[-2] = stack[-2], stack[-1]

    #add the last element in the list to the list again
    elif command == 'DUP' and stack:
        stack.append(stack[-1])

    # get the last 2 elememts in the list, remove them and then apply operator
    elif command in ['+', '-', '*', '/'] and len(stack) > 1:
        a, b = stack.pop(), stack.pop()

        if command == '+':
            stack.append(a + b)
        elif command == '-':
            stack.append(b - a)
        elif command == '*':
            stack.append(a * b)
        elif command == '/':
            stack.append(b // a)
    else:
        print(f"Invalid command or not enough values in the stack: '{command}'")


if __name__ == "__main__":
    main()
