"""
Michael Le
This program is used to find the estimation of pi based on the Gottfried Leibniz rule
pi/4 = 1 - 1/3 +1/5 - 1/7 + 1/9 + 1/11 + 1/13...
It requires the number of iterations in which the user wishes to run the formual with
To print the interations and the estimation we use a while loop
Alternating between addition and subraction, we have to identify which operator to use
Finally formating in order to print the estimation and the number of iteration were on
"""
denom = 1 #Setting the initial demnominator
runValue = 1 #The running value of the estimation
estimate = 0 #The final estimation
iteration = 0 #Number of iterations we are print
n = input("Enter the amount of times you wish to approximate pi: ") #Number of times the user wants to run

print "Iteration\tEstimation" #Formating the answers
print "=========\t=========="

while n > 0: 
    n = n - 1 #Subtracting one from n until it reaches 0 
    iteration = iteration + 1 #Counting up the iterations 
    estimate = runValue * 4 #Final estimate based on the running values
    print "%-9d\t%-f" % (iteration,estimate) #Print formating
    if n == 0: #Stops the program when n reaches 0
        break
    elif (n % 2  !=0): #If the number of iterations left is odd we subtract
        denom = denom + 2 #aggregating the denominator 
        runValue = runValue - (1.0/denom) #finding the estimation while aggregating the value
    else: #If the number of iterations left is even we add
        denom = denom + 2
        runValue = runValue + (1.0/denom) #Same as above but for addition
        
        
        
"""
Programm output:
Enter the amount of times you wish to approximate pi: 20
Iteration	Estimation
=========	==========
1        	4.000000
2        	2.666667
3        	3.466667
4        	2.895238
5        	3.339683
6        	2.976046
7        	3.283738
8        	3.017072
9        	3.252366
10       	3.041840
11       	3.232316
12       	3.058403
13       	3.218403
14       	3.070255
15       	3.208186
16       	3.079153
17       	3.200366
18       	3.086080
19       	3.194188
20       	3.091624

"""
