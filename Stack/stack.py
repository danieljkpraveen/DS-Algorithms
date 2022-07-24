TOP = 0
stack = []


def stack_insert(value):
    stack.insert(TOP, value)

def stact_del():
    stack.pop(TOP)

def print_stack():
    for s in stack:
        print(s)
    print("\n\n")

if __name__ == "__main__":
    program = True
    while program:
        option = int(input("1. Add item\n2. Delete item\n3.Exit\nselect option: "))
        if option == 1:
            value = input("Enter value: ")
            stack_insert(value)
            print(f"stack after insertion:\n")
            print_stack()
        elif option == 2:
            stact_del()
            print(f"stack after deletion at TOP")
            print_stack()
        elif option == 3:
            program = False
        else:
            print("Invalid option\n")