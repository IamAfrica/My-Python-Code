for line in open('Splits.txt'):
    temp = line.split(',')
    name = temp[0].strip()
    age = temp[1].strip()
    print name
    print age