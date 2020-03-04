this_is_an_tuple_packed = (1,2,3,4,5,6,7)
# this_is_an_tuple_unpacked
(one, two, three, four, five,six,seven) = this_is_an_tuple_packed

print(this_is_an_tuple_packed[1:4])
print(one, two, three,four, five)

a=(5,1)
b=(5,4)
if (a>b):print("a is bigger")
else: print("b is bigger")


a = {'x':100, 'y':200}
b = list(a.items())


for key, value in b:
    print (key, value)


print(b) 


"opertor example"
x = 4
y = 8
list = [1, 2, 3, 4, 5 ]
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")


x = 20
y = 20
if ( x is y ): 
	print("x & y  SAME identity")
y=30
if ( x is not y ):
	print("x & y have DIFFERENT identity")
