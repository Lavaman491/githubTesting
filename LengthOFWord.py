# Gives back the length of a given word

print("-Finding the Length of a given word/sentence-")
print('-Leave Blank or Type "quit" to Exit-')
word = input("\n>")

while word.lower() != "quit" and word != "": 
  print(len(word))
  word = input("\n>")
