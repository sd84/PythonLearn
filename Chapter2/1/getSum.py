import sys


def get_sum(nums):
    sum = 0
    for i in nums:
        sum += i
    print("Your sum is ", sum)


def set_sum():
    arr = list()
    try:
        size = input("Enter size of array what you want: ")
        if size.isnumeric():
            size = int(size)
        else:
            raise Exception("size variable is not number. Exit.")
            sys.exit(1)

        for i in range(size):
            val = input("Enter your number: ")
            if val.isnumeric():
                val = int(val)
                arr.append(val)
            else:
                raise Exception("val variable is not number. Exit.")
                sys.exit(1)
    except Exception as text:
        print(text)
    return arr
