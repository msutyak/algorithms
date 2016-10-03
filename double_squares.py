'''
Credits: This challenge appeared in the Facebook Hacker Cup 2011.
A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number of ways in which it can be written as the sum of two squares.

For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2 + 3^2. 
NOTE: Do NOT attempt a brute force approach. It will not work. The following constraints hold: 
0 <= X <= 2147483647 
1 <= N <= 100
'''

#check if an inputted number is a perfect square
def is_perfect_square(n):
    if n<0:
        return False
    else:
        if((int(n**0.5))**2 == n):
            return True
        else:
            return False

'''
Using this logic:
x^2 + y^2 = n
x^2 = n-y^2 
x = sqrt(n - y^2)

x  must be an integer and n - y^2 shoud be a perfect square
'''

def sum_of_squares(n):
    count = 0
    for y in range(0, int(int(n)**0.5)):
        if(is_perfect_square(int(n) - y^2)):
            count += 1
    print count/2
    

