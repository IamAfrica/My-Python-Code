import Rad

def main():
    num = Rad.userList("Enter three numbers, seperated by commas: ")
    for n in num:
        for i in range(0, int(n)):
            print n,
        print 
main()