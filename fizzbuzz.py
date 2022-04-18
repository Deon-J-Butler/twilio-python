import sys

userInput = sys.argv
userInput.pop(0)

for i in userInput:
    if int(i) % 3 == 0:
        if int(i) % 5 == 0:
            print('fizzbuzz')

        else:
            print('fizz')

    elif int(i) % 5 == 0:
        print('buzz')

    else:
        print(i)
