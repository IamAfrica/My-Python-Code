import json
import urllib2

url = "http://www.nactem.ac.uk/software/acromine/dictionary.py?sf=EDU"
jsonTxt = urllib2.urlopen(url).read()
acromine = json.loads(jsonTxt)

print acromine[0]['sf']
for ans in acromine[0]['lfs']:
    print ans['lf']