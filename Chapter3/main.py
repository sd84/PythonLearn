import listCreator


def main():
    count = int(input("Enter list size you want to create:"))
    for i in range(count):
        listCreator.create_list()

    listCreator.show_list()

    choice = input("\nEnter yes if you want to find value\nEnter delete if you want to delete value\n ")
    if choice.lower() == "yes":
        choice = int(input("Enter the value you want to find: "))
        listCreator.find_value(choice)
    elif choice.lower() == "delete":
        choice = int(input("\nEnter the value you want to delete: "))
        listCreator.delete_value(choice)
    else:
        print("Wrong choice.")


if __name__ == "__main__":
    main()
