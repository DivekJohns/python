#define a function
def func1():
   print ("I am learning Python function")
   print ("still in func1")
   
func1()

def square(x):
  	return x*x
print(square(4))

def multiply(x,y=0):
	print("value of x=",x)
	print("value of y=",y)
    
	return x*y
  
print(multiply(y=2,x=4))

def if_else():
	x,y =8,8
	
	if(x < y):
		st= "x is less than y"
	
	elif (x == y):
		st= "x is same as y"
	
	else:
		st="x is greater than y"
	print(st)

if_else()


def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")



print (SwitchExample(1))