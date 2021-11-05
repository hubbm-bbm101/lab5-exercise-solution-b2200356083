maxVal =int (input("Please enter a natural number that is greater than 1: "))
evenSum = 0
oddSum = 0

if maxVal % 2 == 0:
    for i in range(0,maxVal + 1,2):
        evenSum += i
        denum = maxVal/2
    for j in range(1,maxVal,2):
        oddSum += j
    print("Average of all even numbers in the provided interval is " + str(evenSum/denum))
    print("Sum of all odd numbers in the provided interval is " + str(oddSum))        
else:
    for i in range (0, maxVal,2):
        evenSum += i
        denum = (((maxVal - 1) - 2)/2 + 1)
    for j in range(1,maxVal + 1,2):
        oddSum += j
    print("Average of all even numbers in the provided interval is " + str(evenSum/denum))
    print("Sum of all odd numbers in the provided interval is " + str(oddSum))               





       
     
    
        
