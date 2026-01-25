#Miguel Fernandez Brazon
#CSD325-300O Advanced Python
# 1/18/26
#Count Down Bottles Of Beer
def countdown(b):
    #As long as b is bigger than  0 the loop will continue
    while b > 0:
        if b ==1:
            #When is only 1
            print('1 bottle of beer on the wall, 1 bottle of beer')
            print(' take one down and pass it around, no more bottles of beer on the wall')
        else:
            print(b,'Bottles of beer on the wall,', b,'bottles of beer')
            print('Take one down and pass it around,', b - 1 ,'bottles of beer on the wall')
        b = b - 1
        #This one subtract 1 bottle
        #when ending print final comment
#Main Program
#Make the user put how many bottles
    print('Buy more')
n= int(input('bottles of beer on the wall? '))
countdown(n)