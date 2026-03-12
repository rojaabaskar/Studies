'''
def test():
    x = 10      #local variable 
    print(x)

test()'''


x = 10   # global variable

def test():
   global x
   x +=8

