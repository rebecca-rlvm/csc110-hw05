"""
Name: Rebecca
Peers: N/A
References: (anything you checked to solve this)
"""

def get_letter():
    """ Add your own Docstring """
    # remove the default return and add your code
    x = 1
    while x == 1:
        l = input("Give an single uppercase letter: ")
        if len(l) != 1:
            print("Error: it needs to be a single character.")
            continue
        if l == "A" or l == "B" or l == "C":
            return l
            break
        else:
            print("Error: You provided the wrong character.")
            continue

def get_digit():
    """ Add your own Docstring """
    # remove the default return and add your code
    x = 1
    while x == 1:
        d = input("Give an single number character: ")
        if d.isdigit():
            pass
        else:
            print("Error: your input should be only digits.")
            continue
        if d == "1" or d == "2" or d == "3":
            return d
            break
        else:
            print("Error: a single digit needs to be in [1,3].")
            continue


def check_pattern(letter, digit, lst):
    """ Add your own Docstring """
    # remove the default pass and add your code
    
    for i in lst:
        q = "test"
        for n in i:
            if n == letter:
                q = "success"
            if n == digit:
                if q == "success":
                    print(i, end=" ")
                    q = "test"
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

    run = 1
    while run == 1:
        let = get_letter()
        num = get_digit()
        check_pattern(let,num,st_list)
        inpt = input("\n Try Again? (y/n): ")
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