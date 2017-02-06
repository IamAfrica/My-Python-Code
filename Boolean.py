import Rad

#if height is < 54 or age < 14 cannot ride
#if height is == 54 and age == 14 ask person
#if height is > 54 and age > 14 can ride

height = Rad.userFloat("Please enter your height in inches:")
age = Rad.userFloat("Please enter your age:")

if height > 54 and age > 14:
    print "You can ride!"
elif height < 54 or age < 14:
    print "You can't ride..."
elif height == 54 and age == 14:
    print "You must ask to ride"

