def main():
    #defining salary, total and pay
    salary = 0.01
    total = 0
    pay = 0
    #asking user input
    days = int(input('Enter number of days worked: '))
    print('days', 'Pennies')
    print('------------')
    #looping through number of days to find out the pay
    for i in range(1 , days+1):
        pay = salary
        print(i, '\t',pay)
        #increasing salary by 2 times
        salary = salary *2
        #Calculating the total salary
        total+= pay
       # print(salary)
    print('The total salary for ', days,' days is: ',format(total,'.2f'))

main()
