from convert import *


"""
This function takes the input from the user, as it asks for a float. Then, when given the input,
the user will be asked if they want to continue adding. If they decide to keep adding, the user
will continue to be asked if they want to add until they type 'done'. The inputs given are all
checked to see if they are actually floats. If they are, then it is added to the list of floats, 
where it is then returned in the end. If it is not a float, then it will not be added to the list.
The function stops when the user types done.
"""""""""

def gather_numbers() -> list[float]:
    numbers = ""
    listOfNums = []
    while numbers != "done":
        numbers = str(input("Enter a number (or type 'done' when finished: "))
        if str_to_float(numbers) is not None:
            listOfNums.append(str_to_float(numbers))
    return listOfNums

def main():
    print("List of numbers: ", gather_numbers())

if __name__ == '__main__':
    main()