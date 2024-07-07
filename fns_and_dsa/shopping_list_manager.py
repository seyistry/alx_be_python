def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Add item: ")
            shopping_list.append(add_item)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Remove item: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print("item not found")
        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
