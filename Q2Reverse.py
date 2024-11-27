# Create a program that will accept a word and output the word one letter at a time in reverse.
w=str(input("Please enter a word:"))
x=len(w)
for letter in reversed(w):
    print(letter)
print("    ")
