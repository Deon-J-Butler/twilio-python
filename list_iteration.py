import sys

order_of_succession = sys.argv

order_of_succession.pop(0)

x = 1

for name in order_of_succession:
    print(x, name)
    x = x+1