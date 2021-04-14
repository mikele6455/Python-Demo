"""
Michael Le
This program is made in order to calculate a bill for a customer for a loan
We let them input the initial loan amount, the intrest rate and the length of the loan
We then set a variable current so that it will keep track of the amount of money left after caculations
Then we enter the formula to calculate monthy pay over a duration
Printing and formating set up
And finally adding the calculations for each months payment
"""
L = input("Please enter the loan amount: ")
R = input("Please enter the intrest rate in decimals: ")
Y = input("Please enter the length of your loan in months: ")
current = 0 + L 
P = (L*(R*(1+R)**Y))/((1+R)**Y-1)

print "Month\tPrincipal\tInterest\tPrincipal\tNew Balance" #Setting up the table formating with float value
print "     \t         \tPayment \tPayment  \t           "
print "=====\t=========\t========\t=========\t==========="
print "%-5d\t%-8f\t%-8f\t%-8f\t%-11f" % (0,L,0,0,L)
for n in xrange(1,Y+1):#For loop so that we can keep track of n as the number of months
    I = current * R #Formula for interest payments
    C = P - I #Amount of money that goes into the loan exculding the intrest fee
    oldBal = current #We set this so that we can print the old value
    current = current - C #The current amount of loan left that we have to pay
    print "%-5d\t%-8f\t%-8f\t%-8f\t%-11f" % (n,oldBal,I,C,current) #Printing out the information in a formated way

"""
Results data:
Please enter the loan amount: 50000
Please enter the intrest rate in decimals: 0.03
Please enter the length of your loan in months: 24
Month	Principal	Interest	Principal	New Balance
     	         	Payment 	Payment  	           
=====	=========	========	=========	===========
0    	50000.000000	0.000000	0.000000	50000.000000
1    	50000.000000	1500.000000	1452.370797	48547.629203
2    	48547.629203	1456.428876	1495.941921	47051.687281
3    	47051.687281	1411.550618	1540.820179	45510.867102
4    	45510.867102	1365.326013	1587.044784	43923.822318
5    	43923.822318	1317.714670	1634.656128	42289.166190
6    	42289.166190	1268.674986	1683.695812	40605.470378
7    	40605.470378	1218.164111	1734.206686	38871.263692
8    	38871.263692	1166.137911	1786.232887	37085.030805
9    	37085.030805	1112.550924	1839.819873	35245.210932
10   	35245.210932	1057.356328	1895.014469	33350.196463
11   	33350.196463	1000.505894	1951.864904	31398.331559
12   	31398.331559	941.949947	2010.420851	29387.910708
13   	29387.910708	881.637321	2070.733476	27317.177232
14   	27317.177232	819.515317	2132.855480	25184.321752
15   	25184.321752	755.529653	2196.841145	22987.480607
16   	22987.480607	689.624418	2262.746379	20724.734227
17   	20724.734227	621.742027	2330.628771	18394.105457
18   	18394.105457	551.823164	2400.547634	15993.557823
19   	15993.557823	479.806735	2472.564063	13520.993760
20   	13520.993760	405.629813	2546.740985	10974.252776
21   	10974.252776	329.227583	2623.143214	8351.109562
22   	8351.109562	250.533287	2701.837511	5649.272051
23   	5649.272051	169.478162	2782.892636	2866.379415
24   	2866.379415	85.991382	2866.379415	0.000000   
"""
