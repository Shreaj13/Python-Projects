#defining main function 
def main():
    print('Number is prime')
    print('---------------')
    # for loop to loop through the total numbers
    for i in range (1,11):
        # calling is_prime function
        if is_prime(i):
            print(i,'\tprime')
        else:
            print(i,'\tnot prime')

#defining is_prime function to check if the number is prime
def is_prime(number):
    if number == 1:
        return False
    for j in range (2, number):
        if number % j ==0:
            return False
    else:
             return True

main()
