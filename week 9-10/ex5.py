def count_spaces ():  

     # Counts the number of spaces  
    spaces = 0  

    userInput = input("Enter a sentence: ")

    for char in userInput:  

        if char == " ":  

            spaces = spaces + 1  

    return spaces  

print( count_spaces () ) 


