''' Keegan '''
name = input("Enter your name:")
while name == "":
    print("You must enter your name.")
    name = input("Enter your name:")
letter = 1
try:
    for i in range(len(name)):
        print(name[letter])
        letter += 2

except IndexError:
    print("End of name (:")