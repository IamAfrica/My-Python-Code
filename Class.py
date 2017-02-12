def containsNoCase(item, l):
    yes = False
    for x in l:
        if item.upper() == x.upper():
            yes = True
            break
    return yes
    
def intersect(set1, set2):
    result = []
    for i in set1:
        if containsNoCase(i, set2):
            result.append(i)
    return result
        
def union(set1, set2):
    result = []
    
    for i1 in set2:
        if not containsNoCase(i1, result):
            result.append(i1)
    for i2 in set2:
        if not containsNoCase(i2, result):
            result.append(i2)
    return result
    
def readStudents(filename):
    l = []
    file = open(filename)
    for student in file:
        l.append(student.strip())
    return l
    
def main():
    calc = readStudents("calc.txt")
    phys = readStudents("phys.txt")
    bothClasses = intersect(calc, phys)
    eitherClass = union(calc, phys)
    print "%s are in both Calculus and Physics" % bothClasses
    print "%s are in either Calculus or Physics" % eitherClass
    
main()