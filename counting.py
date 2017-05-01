colors = ["blue", "red", "green"]
shapes = ["circle", "square", "triangle"]
texts = ["smooth", "bumpy"]

p = []
for color in colors:
    for text in texts:
        for shape in shapes:
            p.append("%s %s %s" %(color, text, shape))
print len(p)
print p