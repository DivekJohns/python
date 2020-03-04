Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

Dict.update({"Sarah":9})
print(Dict)


del Dict ['Charlie']
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))

for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:       
        print(False)


Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))

print("printable string:%s" % str (Dict))
