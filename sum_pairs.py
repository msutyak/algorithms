'''
You are given a sorted array of positive integers and a number 'X'. 
Print out all pairs of numbers whose sum is equal to X. 
Print out only unique pairs and the pairs should be in ascending order
'''

def sum_numbers(series):
    numbers = series.split(";")[0].split(",")
    sum_target = series.split(";")[1]
    
    i = 0
    j = len(numbers) - 1
    pair_string = ""
    while(i < j):
       if(numbers[i] + numbers[j] == sum_target): 
           pair_string = pair_string + numbers[i] + "," + numbers[j] + ";"
           check = 1
       elif(numbers[i] + numbers[j] <  sum_target):
           i += 1
       elif(numbers[i] + numbers[j] >  sum_target): 
           j -= 1
    if(pair_string == ""):
      print "NULL"
    else:
      print pair_string

#sample input: 2,4,5,6,9,11,15;20
#sample output: 5,15;9,11


