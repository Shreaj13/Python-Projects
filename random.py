#import random
import random
#defining main function
def main():
    # defining a local variable 
    count = 0

    for i in range(1,101):
        number = random.randint(1,100)
        count += isEven(number)
        print(number, '\t',isEven(number))
    print('The count of even number is ', count)
# defining a isEven function
def isEven(num):
    count = 0
    if num % 2 == 0:
        return True
    else:
        return False
#calling the main function
main()
