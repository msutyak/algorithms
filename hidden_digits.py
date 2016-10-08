'''
In this challenge you're given a random string containing hidden and visible digits. 
The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 
1 is behind ' b ' etc., 9 is behind 'j'. Any other symbol in the string means nothing 
and has to be ignored. So the challenge is to find all visible and hidden digits in the 
string and print them out in order of their appearance.
'''

def hidden_digits(sequence):
    s = ""
    digit_dict = {"a": "0", "b": "1", "c": "2", "d": "3", "e": "4", "f": "5", "g": "6", "h": "7", "i": "8", "j": "9"}
    for char in sequence:
        if(char in digit_dict.values()):
            s += char
        elif(char.islower() and char in digit_dict):
            s += digit_dict[char]
    print s