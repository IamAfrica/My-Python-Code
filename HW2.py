#Jordan Darling made this 1/28/16
#Using functions, for loops, and lists to create a song
import Rad

songPt1 = [Rad.userString("Enter the first verse:"), Rad.userString("Enter the second verse:"), Rad.userString("Enter the third verse:"), Rad.userString("Enter the fourth verse:"),]
songPt2 = Rad.userString("Enter the chorus:" ) + " "
repeat = Rad.userInt("Enter the chorus repeat:")
final=[]
print

for part in songPt1:
    chorus = songPt2 * repeat 
    final = songPt1 * 2
    
final.insert(1, chorus)
final.insert(3, chorus)
final.insert(5, chorus)
final.insert(7, chorus + songPt2)
final.insert(8, "... One more time ...")
final.insert(10, chorus)
final.insert(12, chorus)
final.insert(14, chorus)
final.insert(16, chorus + songPt2)

print final

#This prints out the lyrics without the list part
for lyrics in final:
    print lyrics