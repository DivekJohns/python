f = 101
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
  print(f)
  f = "changing global variable"
someFunction()
print(f)
"deltes the variable using del keyword"
# del f
print(f)