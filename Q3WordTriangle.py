# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
x=input("please enter a word: ")
y=0
z=len(x)
while y<=z:
    print(x[0:y])
    y=y+1
print()  
