#! /usr/bin/pyhton3
__name__ = "__main__"
import sys

def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print(f"{num_arguments}", end=' ')
    print("argument" if num_arguments == 1 else "arguments", end='')
    print(":" if num_arguments > 0 else ".")

    counter = 1
    for arg in arguments:
        print(f"{counter}: {arg}")
        counter += 1

                    #OR
    # for i, arg in enumerate(arguments, start=1):
    #     print(f"{i}: {arg}")

                    #OR
    # for counter in range(num_arguments):
    #     print(f"{counter + 1}: {arguments[counter]}")

main()
