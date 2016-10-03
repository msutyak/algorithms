#Capitlize first letter of each word in a sentence

def capitalize(s):
    print ' '.join(word[0].upper() + word[1:] for word in s.split())


