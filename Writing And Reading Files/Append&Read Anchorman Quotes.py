# Code written by Steve O'Gallagher

def createQuotes():
    '''
    Appends Anchorman quotes to the Quotes file.
    '''
    # Prepare the file for appending
    file = open("Quotes.txt", "a+")
    # Prepare the Quotes
    quotes = ["I have many leather-bound books.",
              "I'm not even mad: that's amazing!",
              "Milk was a bad choice.",
              "I'm in a glass case of emotion.",
              "Do you want to come to the pants party?"]
              
    # Write the title for this section
    file.write("Anchorman Quotes\r\n")
       
    # Write in the Anchoman quotes       
    for i in range(5):
        file.write("%d. %s\r\n" % (i+1, quotes[i]))
        
    # Create a blank line at the end of the quotes    
    file.write("\n")
    # Close the file
    file.close()
    
def readQuotes():
    '''
    Reads the Anchorman quotes from the Quotes file
    '''
    # Prepare the file to be read
    file = open("Quotes.txt", "r+")
    # Read the file and save it into memory
    contents = file.read().split("\r\n")
    
    # Create a list from 1-5
    list = [str(x+1) for x in range(5)]
    
    # Find and print all Anchorman quotes in the file
    for i in range(7,len(contents)):
        if contents[i] != "" and contents[i][0] in list:
            print("%s" % (contents[i]))

    # Close the file
    file.close()
    
    
    
if __name__ == "__main__":
    createQuotes()
    print("Anchorman Quotes")
    readQuotes()