import pylab
import numpy as np

def loadFile():
    """
    This function opens up the file containing the temperature data and returns
    the information in the form of a tuple containing two lists.
    high: a list of the high temperatures
    low: a list of the low temperatures
    """
    # Declare variables for high and low temperature lists
    high = []
    low = []
    # Open the file "julyTemps.txt" and save it into variable inFile
    inFile = open("julyTemps.txt","r")
    
    # For each line, add the high and low temperature to the appropriate list
    for line in inFile:
        fields = line.split(" ")
        if len(fields) == 3 and fields[0].isdigit():
                low.append(int(fields[2]))
                high.append(int(fields[1]))
    # Return the data in the form of a tuple
    return (low,high)
            
            
def producePlot(lowtemps, hightemps):
    """
    This function takes in two lists of temperatures and plots them on a graph.
    """
    # Declare the variable diffTemps as a list
    diffTemps = []
    # Determine the difference in the high and low temperatures and store them
    # in the variable diffTemps
    for i in range(len(lowtemps)):
        diffTemps = list(np.array(hightemps) - np.array(lowtemps))
    
    # Create the graph using pylab
    pylab.figure(3)
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel("Days")
    pylab.ylabel("Temperature Ranges")
    pylab.plot(range(31),diffTemps, "bo")
    # Display the graph
    pylab.savefig("TemperatureGraph")

    return
      
# The statements call the functions to read the data and plot the graph                  
t = loadFile()
producePlot(t[0], t[1])
