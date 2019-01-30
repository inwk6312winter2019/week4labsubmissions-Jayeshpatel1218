import string
 
def strip():
    empty = []
    file = open("words.txt","r")
    for line in file:
        res = line.lower().strip(string.punctuation + string.whitespace)
        empty += res
    return empty 
print(strip())
