'''
Alice is looking for a sorority to join for her first year at Acme University. There is a street consisting entirely of sorority houses near the university, and some of her high school friends have already joined sorority houses on the street. (More than one of her friends may live at the same sorority house.)

Alice wants to visit her friends frequently, and needs a program that will help her pick an optimal house to visit them from. Each sorority house has a street number that indicates its location on the street. The optimal location will minimize the sum of differences between the number of Alice's house and the number of her friends' houses.

For example: Alice's friends live at houses 3, 3, 5, and 7. Alice moves in at house 4. Then the distances to her friends' houses are 1, 1, 1, and 3, totaling 6.
'''


import sys

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def min_distance(number_input):
    numbers = number_input.split(" ")
    numbers = [ int(x) for x in numbers ]
    numbers = mergeSort(numbers)
    
    if(len(numbers)%2 == 0):
        index = len(numbers)/2 - 1
        print str(numbers[index])
    else:
        index = int(len(numbers)/2)
        print str(numbers[index]) 

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        min_distance(test)
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...