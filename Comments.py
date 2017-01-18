import math

# Jordan Darling made this on 1/18/16
# This file calculates the volume of a cone

radius = 10
height = 44
    # Calculate the volume of a cone
    # Volume = (pi*height*(radius^2))/3.0
volume = math.pi*(radius*radius)*(height/3.0)
print volume