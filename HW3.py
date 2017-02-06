#Jordan Darling made this 2/5/17
#Using for loops, if statements, and def to calculate values from a list

def readTemps():
    file = open('temps.txt', 'r')
    final = []
    for line in file:
        final.append(float(line))
        
    return final
    

def calculateAvg(temps, start, stop):
    average = 0
    
    while(start <= stop):
        average += temps[start]
        start += 1
    
    average = average/start
    
    return average
  
def count(temps, start, stop):
    x = 0
    
    while(start <= stop):
        if(temps[start] > 0):
            x += 1
        start += 1
    
    return x
    
#It helps to start here and then work your way up
def main():
    temperatures = readTemps()
    deusvult = calculateAvg(temperatures, 0, 80)
    print "During the first 81 years, the average deviation from the temperature anomaly was " + str(deusvult)
    deusvult = count(temperatures, 0, 80)
    print "Durinng the first 81 years, " + str(deusvult) + " had a positive temperature anomaly."
    deusvult = calculateAvg(temperatures, 81, 115)
    print "During the last 35 years, the average deviation from the temperature anomaly was " + str(deusvult)
    deusvult = count(temperatures, 81, 115)
    print "During the last 35 years, " + str(deusvult) + " had a positive temperature anomaly." 

main()