'''
JOLLY JUMPERS
CHALLENGE DESCRIPTION:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla 

A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values 1 through n - 1. eg. 

1 4 2 3 
is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a jolly jumper. 

'''

#takes a space delimited sequence of numbers as a string as input (or from lines from a file)
#e.g. "1 4 2 3"
def jolly_jumper(sequence):
    
    numbers = sequence.split(" ")
    jolly_list = []
    
    for i in range ( len(numbers)-1 ):
        jolly_list.append ( abs( int(numbers[i]) - int(numbers[i+1]) ) )
        
    jolly_list = sorted(jolly_list)
    for difference in range(len(jolly_list)-1) :
        flag = 0
        if difference+1 == jolly_list[difference] :
            flag = 1
        else :
            flag = 0
            print "Not Jolly"
            break
    if flag == 1:
        print "Jolly"