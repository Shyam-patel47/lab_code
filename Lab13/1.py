#Write a program that receives an integer an input. If a string is entered instead of an integer,
# then report an error and give another chance to user to enter an integer. Continue this process 
# till correct input is supplied.
def in_put():
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
        in_put()

in_put()