
x=1
while(x <= 4):
		print(x)
		x += 1

#Define a for loop 
for x in range(2,7):
		print(x)

#use a for loop over a collection
Months = ["Jan","Feb","Mar","April","May","June"]
for m in Months:
		print(m)       

# use the break and continue statements
for x in range (10,20):
			# if (x == 19): break
			if (x % 2 != 0) : continue
			print(x)

#use a for loop over a collection
Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
		print(i+1,m)            