#Write a program which finds the first non-repeated character in a string.

def first_non_repeating(text):
    for char in text:
      count = text.count(char)
      if count == 1:
        print char
        break

#example: first_non_repeating('azxcsdweasdasasdzxasd')
#output:  c

