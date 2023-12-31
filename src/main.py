def main():
    stack = []
    while True:
        try:
            allowed_commands = ['PUSH', 'POP', 'SWAP', 'DUP', '+', '-', '*', '/']

            # User inputs
            user_input = input("Enter a command: ")

            if user_input.startswith('PUSH'):
                process_command(user_input, stack)

            elif user_input in allowed_commands:
                process_command(user_input, stack)
                print(f"Stack is {stack}")
            else:
                print("Invalid Input. Please enter a valid command. 'PUSH', 'POP', 'SWAP', 'DUP', '+', '-', '*' OR '/'")

            print(f"{user_input}")

        except KeyboardInterrupt:
            # handle user tryimg to exit
            print("\nExiting programme..")
            break
        except Exception as e:
            #handle additional exceptions
            print(f"An error has occurred: {e}")


def process_command(command, stack):

    # add number to stack
    if command.startswith('PUSH'):
        if len(command.split()) == 2:
            _, num = command.split()
            if num.isdigit():
                stack.append(int(num))
                print(f'Stack is {stack}')
            else:
                print('Invalid input, please enter an integer')
        else:
            print('Invalid input, please enter PUSH followed by a number')

    #empty stack
    elif command == 'POP' and stack:
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
        print("Invalid command or not enough values in the stack")


if __name__ == "__main__":
    main()
