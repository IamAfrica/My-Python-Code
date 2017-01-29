import Rad

ratings = []
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Bacon']

for flavor in flavors:
    rating = Rad.userString("Rate %s from 1 to 5:" % flavor)
    ratings = ratings + ["%s rated as a %s" % (flavor, rating)]

print ratings