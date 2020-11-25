def main():
    index = 0
    flag = 0
    sign = 1
    sum = 0
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
        y[i][0] = float(input(">"))

    # Calculating the forward difference
    # table
    for i in range(1, n):
         for j in range(n - i):
              y[j][i] = y[j + 1][i - 1] - y[j][i - 1]



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
    for i in range(n):
        print(x[i], end="\t")
        for j in range(n - i):
            print(round(y[i][j], 4), end="\t")
        print("")
##calculating first derivative
    for i in range(1,n-index):
         term = y[index][i] / i
         sum = sum + sign*term
         sign = -sign

    first_derivative = round((sum/h),4)
    print("Reqd value is", first_derivative)


 ##second derivative
    sign = 1
    sum = 0
    pattern = [1, 1, 11 / 12, 5 / 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(2, n - index):
        term = y[index][i] * pattern[i - 2]
        sum = sum + sign * term
        sign = -sign
    second_derivative = round((sum / (h * h)), 4)
    print("Reqd value is", second_derivative)


    again = input("Do you want to try-again for another data sets?")
    if again.lower()=="y" or again.lower() == 'yes':
        main()
    else:
        print('*'*10+'Exiting Application'+'*'*10)



if __name__ == "__main__":
    main()


