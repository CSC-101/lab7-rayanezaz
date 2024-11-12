import sys
from convert import str_to_float

""'"'"""""""""
This function takes the sys.argv that is called, and then it checks to see if each value in the list
is a float. If the value is a float, then it is added to the total. However, if the value is not a float,
then the function will still go through the other values in the list, and will return the total value for
the float values added up.
"""""""""


if __name__ == '__main__':
    print(sys.argv)
    y = 0
    for x in range(1, len(sys.argv)):
        val = str_to_float(sys.argv[x])
        if val is not None:
            y += val
    print(round(y, 3))