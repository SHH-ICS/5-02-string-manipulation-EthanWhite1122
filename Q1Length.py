# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
w=str(input("Please enter a word:"))
try: 
    x=int(w)
    print("Enter a word please")
except ValueError:
    l=len(w)
    print("The word" , w , "is" , l  ,"letters long!")
