import json


x = """

[{"price": " 40.50 ",    "qty": "   1  ",  "desc": "  Arm Rest  ",  "code": " 234  "}] """

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(type(y))

## just for the first list 
print(y[0])

totalQty = 0 

for oneRecord in y:
    print(oneRecord)
    # just select the qty 
    print(oneRecord['qty'])
    ## add the qty to the running total 
    
    totalQty += float(oneRecord[qty])
    
print("total qty is" + str (totalQty)) 