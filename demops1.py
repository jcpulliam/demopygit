import math 
import numpy



#Problem 2.1
deposit1=1000 #deposit of $1000
interest1=0.05 #interest rate of 5%
time1=10 #number of years = 10 
wealth1 = "${:,.2f}".format(numpy.round(deposit1*(1+interest1)**time1,2))
print ("2.1: Bill's total wealth is", wealth1 + ".")
#Wealth = Deposit x (1 + Interest rate)^Time 
