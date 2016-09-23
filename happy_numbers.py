#Happy Numbers Alogirthm

'''
A happy number is defined by the following process. 
Starting with any positive integer, replace the number 
by the sum of the squares of its digits, and repeat the 
process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy 
numbers, while those that do not end in 1 are unhappy numbers.
'''

#takes an int and an empty list (to keep track of sums over the recursive function)
def happy_number(num, tracking_list = []):
    if (num == 1):
        print 1
    else:
        digit_list = map(int, str(num)) 
        digit_sum = 0
        for n in digit_list:
            digit_sum = (n ** 2) + digit_sum
        if digit_sum in tracking_list:
            print 0
        else:
            tracking_list.append(digit_sum)
            happy_number(digit_sum, tracking_list)