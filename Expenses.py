import Rad

kmWeekday = Rad.userInt("How many kilometers did you travel on a weekday?")
kmWeekend = Rad.userInt("How many kilometers did you travel on a weekend?")

miWeekday = Rad.kmToMi(kmWeekday)
miWeekend = Rad.kmToMi(kmWeekend)

dollarsWeekday = miWeekday * 0.13
dollarsWeekend = miWeekend * 0.24

print "Weekday $%.2f" % dollarsWeekday
print "Weekend $%.2f" % dollarsWeekend
print "Total $%.2f" % (dollarsWeekday * dollarsWeekend)