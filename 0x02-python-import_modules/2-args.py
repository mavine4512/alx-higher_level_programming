#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numCount = len(sys.argv) - 1
    if numCount == 0:
        print("0 arguments")
    elif numCount == 1:
        print("1 argument")
    else:
        print("{} arguments".format(numCount))
    for i in range(numCount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
