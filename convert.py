## dictionary where the line from 
## text will be stored 


dict1 = {}
  
# creating dictionary
with open('products.txt') as fh:
    head = '['
    body = ''
    for line in fh:
        description = line.strip()
        # break on the dash to make array
        items = description.split("-")
 
        item1 = items.pop()
        item2 = items.pop()
        item3 = items.pop()
        item4 = items.pop()
        
        output = '{'
        output+= f' "price": "{item1} ",   '
        output+= f' "qty": "  {item2} ", ' 
        output+= f' "desc": " {item3} ", '
        output+= f' "code": " {item4} "       '
        
        output += '},'
        body += output
    body = body[0:-1]    
    footer = ']'
    
    
    total = head + body + footer
    
    print(total)