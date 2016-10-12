'''
CHALLENGE DESCRIPTION:

In this challenge you need to find the longest word in a sentence. 
If the sentence has more than one word of the same length you should pick the first one.
'''

def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""
    for word in words:
        if (len(word) > len(longest)):
            longest = word
    print longest