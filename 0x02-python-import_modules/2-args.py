#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv) -1
    if lenght == 0:
        print("{} arguments.".format(lenght))
    elif lenght == 1:
        print("{} argument:".format(lenght))
    else:
        print("{} arguments:".format(lenght))
    for i in range(1,lenght):
        print("{}: {}".format(i, sys.argv[i]))
