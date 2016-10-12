
'''
Your good friend Tom is admirer of tasting different types of fine wines. 
What he loves even more is to guess their names. One day, he was sipping 
very extraordinary wine. Tom was sure he had tasted it before, but what 
was its name? The taste of this wine was so familiar, so delicious, so 
pleasant… but what is it exactly? To find the answer, Tom decided to taste 
the wines we had. He opened wine bottles one by one, tasted different varieties 
of wines, but still could not find the right one. He was getting crazy, “No, 
it’s not that!” desperately breaking a bottle of wine and opening another one. 
Tom went off the deep end not knowing what this wine was. Everything he could say 
is just several letters of its name. You can no longer look at it and decided to 
help him.  Your task is to write a program that will find the wine name, containing 
all letters that Tom remembers.
'''

#recursive function 
def guess_wine(wine_input):
    l = wine_input.split(" | ")
    wines = l[0].split(" ")
    remembered = l[1].strip()
    
    new_string = ""
    
    for wine in wines:
        if(remembered[0] in wine):
            new_string = new_string + wine + " "
    if new_string=="":
        print False
    else:
        if (len(remembered) == 1):
            print new_string
        else:
            guess_wine(new_string + " | " + remembered[1:])


'''
Example Input:
Cabernet Merlot Noir | ot
Chardonnay Sauvignon | ann
Shiraz Grenache | o
'''