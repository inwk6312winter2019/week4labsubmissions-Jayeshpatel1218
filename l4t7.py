import string
def rename(word):
    punc = string.punctuation
    stri = ""
    for p in punc:
        stri = word.strip()
        stri = word.replace(p,'')
    print(stri)
    return stri

def sed(filename1,filename2):
     try:
        master = open(filename1,"r")
        slave = open(filename2,"w")
        for ma in master:
            new = rename(ma)
            slave.write(ma)
        print("File write operation completed successfully :-)")
     except:
        print("Oops something went wrong!!!")


a = input("Enter master file:")
b = input("Enter slave file:")
sed(a,b)

