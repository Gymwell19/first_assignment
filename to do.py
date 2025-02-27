#initialize an empty list to store the to do items
todo_list = []

#function to add a new item to the to do list
def add_item(item):
    todo_list.append(item)
    print(f"Added: {item}")

    #Function to view the curent to do list
def view_list():
    if not todo_list:
        print("No items in the list")
    else:
        print("To do list:")
        for i, item in enumerate(todo_list):
            print(f"{i+1}. {item}")

            #Function to remove an item from the to do list
def remove_item(index):
    try:
        index = int(index) - 1
        remove_item = todo_list.pop(index)
        print(f"Removed: {remove_item}")
    except IndexError:
        print("Invalid item number")
    except ValueError:
        print("That is not a valid number.")

        #Main loop to interact with the user
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter item to add: ")
        add_item(item)
    elif choice == "2":
        view_list()
    elif choice == "3":
        index = input("Enter item number to remove: ")
        remove_item(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
        