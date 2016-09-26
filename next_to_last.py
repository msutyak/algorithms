#Write a program which finds the next-to-last word in a string.

#Takes a string as an input
def next_to_last(text):
    if(len(text.split()) > 1):
        print text.split()[-2]
    else:
        print text
        
#prints "is"
next_to_last("this is great")

