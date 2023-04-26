#Defining main function
def main():
    #asking for user input
    budget = int(input('Enter the budget for the month: '))
    #displaying value to stop the loop
    print('Enter 0 to exit')
    total = 0

    amount_spent = 1
    while amount_spent != 0:
        amount_spent = int(input('Enter the expenses: '))
        total += amount_spent
    print('Your budget is:', budget)
    print('Your total expenses is:', total)
    if budget > total:
        print('Well done')
    else:
        print('Plan better next time')


main()
