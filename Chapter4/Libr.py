def create_lib(val):
    lib = {}
    for x in range(val):
        lib[input("Enter key value: ")] = input("Enter value for key: ")
    return lib


def show_lib(lib):
    for x, y in lib.items():
        print("lib[" + x + "] = " + y)


