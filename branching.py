import sys

theSum = sys.argv

if int(theSum[1]) + int(theSum[2]) <= 0:
    print('You have chosen the path of destitution.')

elif 100 >= int(theSum[1]) + int(theSum[2]) > 0:
    print('You have chosen the path of plenty.')

else:
    print('You have chosen the path of excess.')
