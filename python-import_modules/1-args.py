#! /usr/bin/python3
__name__ == "__main__"
string_input = input("")
arguments = string_input.split(" ")
no_of_arguments = len(arguments)
counter = 1
if arguments == ['']:
    print("{} arguments.".format(0), end="\n")
elif no_of_arguments == 1:
    print("{} argument:".format(no_of_arguments), end="\n")
    for argument in arguments:
        print("{}: {}".format(counter, argument), end="\n")
else:
    print("{} arguments:".format(no_of_arguments), end="\n")
    for argument in arguments:
        while counter <= no_of_arguments:
            argument = arguments[counter -1]
            print("{}: {}".format(counter, argument), end="\n")
            nth = arguments[counter - 1]
            argument = nth
            counter += 1