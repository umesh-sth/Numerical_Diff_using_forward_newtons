#from tabulate import tabulate
def main():
    index = 0
    flag = 0
    sign = 1
    sum = 0
    num=0
    print('*' * 10 + 'Numerical Differentiation Calculator (using Newtons forward formula)' + '*' * 10)
    n = int(input("Enter the number of data sets you want to enter:"))

    #getting x values
    x= []
    input_x = str(input("Enter values of x separated using commas:"))
    list_x = input_x.split(",")
    for i in list_x:
        x.append(float(i))

    #getting y value points
    y = [[0 for i in range(n)]for j in range(n)]
    print("Enter the y-value one by one orderly! BE CAREFULL")
    for i in range(n):
        y[i][0] = float(input(f'- y[{i}] >'))

    # Calculating the forward difference table

    for i in range(1, n):
         for j in range(n - i):
              y[j][i] = round(y[j + 1][i - 1] - y[j][i - 1], 4)



  ##validating point of differentiation
    while(flag ==0):

        num = float(input("Enter where you want to find the differentiation:"))
        for i in range(0,n-1):
             if ((abs(num-x[i])) <0.0001):
                 index = i
                 flag = 1

        if(flag ==0):
             print("Invalid Calculation point. This point should be nearer to the x_points and can differ only by 0.0001")

 #calculating h
    h = x[1] - x[0]

    # Displaying the forward difference table
    print('*' * 10 + 'Displaying forward difference table' + '*' * 10)
    print('\n\n')
    for i in range(n):
        print(x[i], end="\t\t")
        for j in range(n - i):
            print("{:.4f}".format(round(y[i][j], 4)), end="\t\t")
        print("")
    print('\n\n')
    # tabulate_data = input('DO you want to print this in tabulated form?')
    # if tabulate_data.lower() =='y' or tabulate_data.lower()=='yes':
    #     print('*' * 10 + 'Displaying forward difference table' + '*' * 10)
    #     #table = zip(x,y)
    #     print(tabulate(y,tablefmt="github"))
##calculating first derivative
    for i in range(1,n-index):
         term = y[index][i] / i
         sum = sum + sign*term
         sign = -sign

    first_derivative = round((sum/h),4)
    print(f'Reqd value of first derivative at point {num}  is {first_derivative} \n')


 ##second derivative
    sum = 0
    pattern = [1, -1, 11 / 12, -5 / 6, 0.761, -0.7, 0.648, -0.603]
    terminator = 0
    if (n-index-1)<9:
        terminator = n-index-1
    else:
        terminator=9
    for i in range(1,terminator):
        sum = sum + (y[index][i+1] * pattern[i - 1])
    second_derivative = round((sum / (h * h)), 4)
    print(f'Reqd value of second derivative at point {num} is {second_derivative} \n')



    again = input("Do you want to try-again for another data sets?")
    if again.lower()=="y" or again.lower() == 'yes':
        main()
    else:
        print('*'*10+'Exiting Application'+'*'*10)



if __name__ == "__main__":
    main()


