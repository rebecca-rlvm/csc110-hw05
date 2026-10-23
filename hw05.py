"""
Name: Rebecca
Peers: N/A
References: Slides
"""

def get_letter():
    """ Get an input from the user that needs to be a capital and uppercase A, B, or C.
    If it does not meet those requirements, the function loops until it gets a good
    input. """
    # remove the default return and add your code
    
    # Setting up an infinite loop
    x = 1
    while x == 1:
        # Getting user input
        l = input("Give an single uppercase letter: ")
        # Printing an error message and looping if the input is not one letter
        if len(l) != 1:
            print("Error: it needs to be a single character.")
            continue
        # If the input is good the loop is broken
        if l == "A" or l == "B" or l == "C":
            return l
            break
        # If the input is not "A," "B," or "C," prints an error message and loops
        else:
            print("Error: You provided the wrong character.")
            continue

def get_digit():
    """ Gets an input from the user that must be a single digit between [1,3].
    If the input does not meet those requirements, the function loops until it
    gets a good input. """
    # remove the default return and add your code
    
    # Setting up an infinite loop
    x = 1
    while x == 1:
        # Getting user input
        d = input("Give an single number character: ")
        # Continueing if the input is a digit, otherwise printing an error and looping
        if d.isdigit():
            pass
        else:
            print("Error: your input should be only digits.")
            continue
        # If the input is good, returns the varaible
        if d == "1" or d == "2" or d == "3":
            return d
            break
       # If the input is not within [1,3], prints an error message and loops 
        else:
            print("Error: a single digit needs to be in [1,3].")
            continue


def check_pattern(letter, digit, lst):
    """ Searches the list for when the letter followed by the digit appears in
    a string and prints those values."""
    # remove the default pass and add your code
    
    # Printing the start of the message
    print("Strings with the pattern:")
    # Looking at every string in the list
    for i in lst:
        # Setting up a variable that will change if the inputed letter is in the string
        q = "test"
        # Looking at each character in each string
        for n in i:
            # If the letter appears, 'q' becomes 'success', which can be used to see if the letter appeared before the number
            if n == letter:
                q = "success"
            # If the digit appears and the letter has already appeared...
            if n == digit:
                if q == "success":
                    # Prints the string with a space
                    print(i, end=" ")
                    # Changes q back to its OG state so it can be used to test future strings
                    q = "test"
                    # Changing a global variable so that an extra enter is included if a string was printed
                    global var
                    var = "pass"
                    break
                else:
                    continue
            else:
                continue

#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Setting up an infinite loop
    run = 1
    while run == 1:
        global var
        var = "fail"
        let = get_letter()
        num = get_digit()
        check_pattern(let,num,st_list)
        if var == "pass":
            inpt = input("\nTry Again? (y/n): ")
        else:
            inpt = input("Try Again? (y/n): ")
        if inpt == "y" or inpt == "Y":
            continue
        if inpt == "n" or inpt == "N":
            run = 0
    
    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()