def main():
    d = {}
    for line in open("sss.txt"):
        lst = line.split(',')
        sem = lst[0].strip()
        cls = lst[1].strip()
        if sem in d:
            d[sem].append(cls)
        else:
            d[sem] = [cls]
    
    for key in d.keys():
        print "%s: %s" % (key, d[key])
        
main()