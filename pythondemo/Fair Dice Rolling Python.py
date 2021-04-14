import random #importing random module

n            = 60 #number for for loop
count        = 0 #counting for table listing
sideOne      = 0.00 #counting the number of times the die lands on one side
sideTwo      = 0.00
sideThree    = 0.00
sideFour     = 0.00
sideFive     = 0.00
sideSix      = 0.00

print "Number of times\tResult\tResult Track" #formatting
print "===============\t======\t============"

for amount in range(n): #for loop to keep rolling n number of times
    roll  = random.randint(1,6) 
    count = count + 1 
    if roll  == 1: #if statements to show results if the die rolls on one side
        sideOne = sideOne + 1
        print "%-15d\t%-6d\t%-12d" % (count, roll, sideOne)
    elif roll == 2:
        sideTwo   = sideTwo + 1
        print "%-15d\t%-6d\t%-12d" % (count, roll, sideTwo)
    elif roll == 3:
        sideThree = sideThree + 1
        print "%-15d\t%-6d\t%-12d" % (count, roll, sideThree)
    elif roll == 4:
        sideFour = sideFour + 1
        print "%-15d\t%-6d\t%-12d" % (count, roll, sideFour)
    elif roll == 5:
        sideFive = sideFive + 1
        print "%-15d\t%-6d\t%-12d" % (count, roll, sideFive)
    elif roll == 6:
        sideSix = sideSix + 1
        print "%-15d\t%-6d\t%-12d" % (count, roll, sideSix) 

percentage1 = (sideOne/n)   * 100 #calculating percentage of how often the die roll on one side
percentage2 = (sideTwo/n)   * 100
percentage3 = (sideThree/n) * 100
percentage4 = (sideFour/n)  * 100
percentage5 = (sideFive/n)  * 100
percentage6 = (sideSix/n)   * 100
print "Side 1 percentage: ", percentage1, "Side 2 percentage: ", percentage2, "Side 3 percentage: ", percentage3, "Side 4 percentage: ", percentage4, "Side 5 percentage: ", percentage5, "Side 6 percentage: ", percentage6  
#printing results
"""
Conclusion: Using scientific principles, I can conclude the the higher the number of times we roll the die, the more accurate each side of  the die to 16.666%.

n = 6:
Number of times	Result	Result Track
===============	======	============
1              	6     	1           
2              	1     	1           
3              	3     	1           
4              	5     	1           
5              	1     	2           
6              	1     	3           
Side 1 percentage:  50.0 Side 2 percentage:  0.0 Side 3 percentage:  16.6666666667 Side 4 percentage:  0.0 Side 5 percentage:  16.6666666667 Side 6 percentage:  16.6666666667


n = 60:
Number of times	Result	Result Track
===============	======	============
1              	4     	1           
2              	3     	1           
3              	5     	1           
4              	3     	2           
5              	1     	1           
6              	1     	2           
7              	4     	2           
8              	3     	3           
9              	6     	1           
10             	4     	3           
11             	2     	1           
12             	2     	2           
13             	6     	2           
14             	3     	4           
15             	1     	3           
16             	3     	5           
17             	6     	3           
18             	3     	6           
19             	4     	4           
20             	1     	4           
21             	4     	5           
22             	1     	5           
23             	6     	4           
24             	5     	2           
25             	2     	3           
26             	6     	5           
27             	3     	7           
28             	5     	3           
29             	6     	6           
30             	6     	7           
31             	2     	4           
32             	1     	6           
33             	5     	4           
34             	3     	8           
35             	6     	8           
36             	6     	9           
37             	6     	10          
38             	2     	5           
39             	2     	6           
40             	4     	6           
41             	4     	7           
42             	1     	7           
43             	4     	8           
44             	6     	11          
45             	1     	8           
46             	3     	9           
47             	6     	12          
48             	6     	13          
49             	5     	5           
50             	6     	14          
51             	6     	15          
52             	3     	10          
53             	5     	6           
54             	3     	11          
55             	2     	7           
56             	6     	16          
57             	6     	17          
58             	2     	8           
59             	3     	12          
60             	2     	9           
Side 1 percentage:  13.3333333333 Side 2 percentage:  15.0 Side 3 percentage:  20.0 Side 4 percentage:  13.3333333333 Side 5 percentage:  10.0 Side 6 percentage:  28.3333333333
