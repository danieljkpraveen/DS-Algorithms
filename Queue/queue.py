HEAD = -1
TAIL = 0
queue = []

def enqueue(value):
    queue.insert(TAIL, value)

def dequeue():
    queue.pop(HEAD)

def print_queue():
    for q in queue:
        print(q)
    print("\n\n")


if __name__ == "__main__":
    program = True
    while True:
        option = int(input("1. Add item\n2. Delete item\n3.Exit\nselect option: "))
        if option == 1:
            value = input("Enter value: ")
            enqueue(value)
            print(f"queue after insertion at TAIL:\n")
            print_queue()
        elif option == 2:
            dequeue()
            print(f"queue after deletion at HEAD")
            print_queue()
        elif option == 3:
            program = False
        else:
            print("Invalid option\n")