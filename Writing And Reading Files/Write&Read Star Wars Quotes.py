# Code written by Steve O'Gallagher

def createFile():
    '''
    Creates a file called "Quotes.txt" and writes Star Wars quotes into the file.
    '''
    # Prepare the file for writing
    file = open("Quotes.txt", "w+")
    # Write a title for the quotes into the file
    file.write("Star Wars Quotes\r\n")
    
    # Prepare the Star Wars quotes
    quotes = ["Do or do not, there is no try.",
              "Boring conversation anyway.",
              "I am your father.",
              "That's no moon.",
              "I thought they smelt bad on the outside."]
              
    # Write the Star Wars quotes into the file
    for i in range(5):
        file.write("%d. %s\r\n" % (i+1,quotes[i]))
        
    # Create a blank line at the end of the quotes  
    file.write("\n")
    # Close the file 
    file.close()
 
def readFile():
    '''
    Reads the Star Wars quotes from the Quotes file
    '''
    # Prepare the file to be read
    file = open("Star Wars Quotes.txt", "r")
    # Read the file and save it into memory
    contents = file.read().split("\r\n")
    
    # Create a list from 1-5
    list = [str(x+1) for x in range(5)]

    # Find and print all quotes in the file
    for i in range(len(contents)):
        if contents[i] != "" and contents[i][0] in list:
                print("%s" % (contents[i]))
    
    # Close the file
    file.close()
    
    
    
if __name__ == "__main__":
    createFile()
    print("Star Wars Quotes")
    readFile()
