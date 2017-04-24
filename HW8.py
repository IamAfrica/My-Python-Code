# Jordan Darling made this 4/23/17 using json from web principles
# A relatively easy program, 2 functions would have sufficed
import Rad
import json
import urllib2

# Retrieves the online json information
def getJson(abb):
    abb = abb
    url = "https://api.apixu.com/v1/current.json?key=07a8b12e947948c0a51234815172304&q=" + abb
    
    return urllib2.urlopen(url).read()
    
# Prints resulting text
def printWeather(api):
    api = api
    
    print "Here is the current weather for %s, %s\n%s and %s (F)\nIt actually feels like %s (F)" %(api['location']['name'], api['location']['region'], api['current']['condition']['text'], api['current']['temp_f'], api['current']['feelslike_f'])
    
def main():
    go = True
    while go == True:
        abb = Rad.userString("Please enter a zipcode or city name:")
        jsonTxt = getJson(abb)
        api = json.loads(jsonTxt)
        printWeather(api)
        
        temp = Rad.userString("Want to check another location? (y/n):")
        
        if temp == 'n':
            go = False
    
main()