#Write a program to determine the largest sum of contiguous integers in a list.

def get_max_sum(numbers):
    number_list = numbers.split(",")
    max_sum = 0
    running_sum = 0
    for num in reversed(number_list):
        running_sum = running_sum + int(num)
        if (max_sum < running_sum):
            max_sum = running_sum
        elif (running_sum < 0):
            running_sum = 0
    print max_sum

    #example: -10,2,3,-2,0,5,-15
    #output: 8