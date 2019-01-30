import string 
def frequent_words():
  empty = []
  file = open("words.txt",'r')
  r = file.readlines()
  for line in r:
    res = line.lower().strip(string.punctuation + string.whitespace)
    empty += res

  max = 3
  for u in empty :
    if empty.count(u) > max:
      max = empty.count(u)
      print(u)
  print(max)


print(frequent_words())

