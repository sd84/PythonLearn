lst = list()


def create_list():
    value = input("Enter your value: ")
    if value.isnumeric():
        lst.append(int(value))
    else:
        lst.append(value)


def find_value(text):
    if text in lst:
        print("Success! Find a value")
    else:
        print("Unfortunately value is not in list")


def show_list():
    if len(lst) > 0:
        for x in lst:
            print(x, end=" ")
    else:
        print("The list is empty! Please create before using")


def delete_value(value):
    if value in lst:
        index = lst.index(value)
        print("The value ", lst.pop(index), " was removed.")
        show_list()
    else:
        print("The value - ", value, " is not in list")
