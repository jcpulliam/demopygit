touch ps_1/ps1.py 
import math 
import numpy



#Problem 2.1
deposit1=1000 #deposit of $1000
interest1=0.05 #interest rate of 5%
time1=10 #number of years = 10 
wealth1 = "${:,.2f}".format(numpy.round(deposit1*(1+interest1)**time1,2))
print ("2.1: Bill's total wealth is", wealth1 + ".")
#Wealth = Deposit x (1 + Interest rate)^Time 

#Problem 2.2
#How long does it take Bill to double his money?
double = numpy.round(math.log10(2)/math.log10((1+interest1)),2)
print ("2.2: It takes Bill",double, "years to double his money.")

#Problem 2.3
#Does Jack double his money in 6 years?
deposit2 = 1000 #deposit of $1000
interest2 = 0.2 #interest rate of 20% 
time2 = 6 #number of years = 6
wealth2 = (numpy.round(deposit2*(1+interest2)**time2)) 
#Wealth = Deposit x (1 + Interest rate)^Time 

currency = "${:,.2f}".format(wealth2) #formating how currency appears 

if wealth2 > 2 * deposit2:
    print("2.3: True, Bill has",currency+".")
else:
    print("2.3: False, Bill has",currency+".")


#If wealth doubles in six years, it will appear as true. 
#If wealth does not double in six years, it will appear as false. 


#Problem 2.4
#Create list of amounts saved in Savings account
Savings = ['Bill', 1000, 'Jack', 5000, 'Amy', 6700, 'Cindy', 5699, 'Harry', 6700]
print("2.4:", Savings)
#A list is a collectio nof ordered data compared to a set which is
#an unordered collection of data. 


#Problem 2.5
#Create Dictionary called "Account"
Accounts = {'Bill': 1000, 'Jack': 5000, 'Amy': 6700, 'Cindy': 5699, 'Harry': 6700}
print ("2.5:", Accounts)
#A dictionary is an unordered collection of data 
#that stores that data in key-value pairs.


#Problem 2.6
#Create List of tuples
savingstuple=('(Bill, 1000),' '(Jack, 5000),' '(Amy, 6700),' '(Cindy, 5699),' '(Harry, 6700)')
print("2.6:", savingstuple)
#A list and tuple is a collection of ordered data.

