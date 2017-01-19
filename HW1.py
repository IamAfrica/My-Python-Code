# Jordan Darling made this 1/18/16
# Create a recipe convertor with an adjustible factor

print "-- ORIGINAL RECIPE --";

print "Enter the amount of flour (cups):",
flour = float (raw_input())

print "Enter the amount of water (cups):",
water = raw_input()

print "Enter the amount of salt (teaspoons):",
salt = raw_input()

print "Enter the amount of yeast (teaspoons):",
yeast = raw_input()

print "Enter the loaf adjustment factor (e.g. 2.0 double the size):",
factor = raw_input()

print "-- MODIFIED RECIPE --"

print "Breadflour: %.2f cups" % (int(flour)*int(factor))

print "Water: %.2f cups" % (int(water)*int(factor))

print "Salt: %.2f teaspoons" % (int(salt)*int(factor))

print "Yeast: %.2f teaspoons" % (int(yeast)*int(factor))

print "HAPPY CODING!"