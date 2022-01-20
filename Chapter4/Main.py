import Tuples as tpl
import Libr


def main():
    new_tpl = tpl.create_tuple(int(input("Enter tuple capacity you want: ")))
    new_lib = Libr.create_lib(int(input("Enter library capacity you want: ")))
    print("Before optimize")
    tpl.show_tuple(new_tpl)
    tmp = tpl.optimize_tuple(new_tpl)
    print("\nAfter optimize")
    tpl.show_tuple(tmp)
    print("\n")
    Libr.show_lib(new_lib)


if __name__ == "__main__":
    main()
