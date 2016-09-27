#Write a program which sorts numbers.

#takes an input of a text string or a file with a list of number floats
def number_sort(text):
    num_split = text.split()
    num_split.sort(key=float)
    join_str = ' '.join(num_split)
    print join_str


#sample input: "70.920 -38.797 14.354 99.323 90.374 7.581 -37.507 -3.263 40.079 27.999 65.213 -55.552"