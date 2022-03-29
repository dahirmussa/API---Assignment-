import logging
import json
import requests

from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})



@app.route('/getStockIDs')
def getStockIDs():


    x = """
    [{ "price": " 40.50 ",    "qty": "   1  ",  "desc": "  Arm Rest  ",  "code": " 234  "       },{ "price": " 20.10 ",    "qty": "   4  ",  "desc": "  Bench seat  ",  "code": " 1351  "       },{ "price": " 5.10 ",    "qty": "   4  ",  "desc": "  Bucket seat  ",  "code": " 453411  "       },{ "price": " 20.50 ",    "qty": "   5  ",  "desc": "  Children and baby car seat  ",  "code": " 7811  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Fastener  ",  "code": " 13231  "       },{ "price": " 22.10 ",    "qty": "   5  ",  "desc": "  Headrest  ",  "code": " 23411  "       },{ "price": " 120.10 ",    "qty": "   10  ",  "desc": "  Seat belt  ",  "code": " 11  "       },{ "price": " 34.10 ",    "qty": "   22  ",  "desc": "  Seat bracket  ",  "code": " 181  "       },{ "price": " 230.10 ",    "qty": "   30  ",  "desc": "  Seat cover ",  "code": " 711  "       },{ "price": " 23.10 ",    "qty": "   50  ",  "desc": "  Seat track  ",  "code": " 14561  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Other seat components  ",  "code": " 1134  "       },{ "price": " 202.10 ",    "qty": "   10  ",  "desc": "  Back seat  ",  "code": " 11311  "       },{ "price": " 210.10 ",    "qty": "   11  ",  "desc": "  Front seat  ",  "code": " 234234  "       }] """
    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(type(y))

    ## just for the first list 
    print(y[0])

    totalStockID = 0 

    for oneRecord in y:
        print(oneRecord)
        # just select the qty 
        print(oneRecord['stocks'])
        ## add the qty to the running total 
        
        buffer = ''
        buffer += oneRecord['stocksID'] + ','
        totalStockID += float(oneRecord[qty])
        
    print("total StocksIDs is" + str (totalStockID)) 
    return jsonify(buffer + '' + str (totalStockID))



@app.route('/getStockNames')
def getstocknames():
    x = """
    [{ "price": " 40.50 ",    "qty": "   1  ",  "desc": "  Arm Rest  ",  "code": " 234  "       },{ "price": " 20.10 ",    "qty": "   4  ",  "desc": "  Bench seat  ",  "code": " 1351  "       },{ "price": " 5.10 ",    "qty": "   4  ",  "desc": "  Bucket seat  ",  "code": " 453411  "       },{ "price": " 20.50 ",    "qty": "   5  ",  "desc": "  Children and baby car seat  ",  "code": " 7811  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Fastener  ",  "code": " 13231  "       },{ "price": " 22.10 ",    "qty": "   5  ",  "desc": "  Headrest  ",  "code": " 23411  "       },{ "price": " 120.10 ",    "qty": "   10  ",  "desc": "  Seat belt  ",  "code": " 11  "       },{ "price": " 34.10 ",    "qty": "   22  ",  "desc": "  Seat bracket  ",  "code": " 181  "       },{ "price": " 230.10 ",    "qty": "   30  ",  "desc": "  Seat cover ",  "code": " 711  "       },{ "price": " 23.10 ",    "qty": "   50  ",  "desc": "  Seat track  ",  "code": " 14561  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Other seat components  ",  "code": " 1134  "       },{ "price": " 202.10 ",    "qty": "   10  ",  "desc": "  Back seat  ",  "code": " 11311  "       },{ "price": " 210.10 ",    "qty": "   11  ",  "desc": "  Front seat  ",  "code": " 234234  "       }]"""
    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(type(y))

    ## just for the first list 
    print(y[0])

    totalStocknames = 0 

    for oneRecord in y:
        print(oneRecord)
        # just select the qty 
        print(oneRecord['stockname'])
        ## add the qty to the running total 
        
        buffer = ''
        buffer += oneRecord['stockname'] + ','
        totalprice += float(oneRecord[stockname])
        
    print("total stock name is" + str (totalStocknames)) 
    return jsonify(buffer + '' + str (totalStocknames))
    
  


@app.route('/getalldataRPC')
def getalldatarpc():

    ## this login 
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('called back json pc server')
    url = "http://localhost:4000/jsonrpc" ## url for the local host 

    # Example calling the echo method
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(url, json=payload).json()
    buffer = '' 
    buffer += str(response)  ## adding the response to the buffer 
    buffer += response['result']
 
    logging.info('finish calling back')
    return jsonify(buffer)

 

@app.route('/getQty')
def getqty():

     
    x = """
    [{ "price": " 40.50 ",    "qty": "   1  ",  "desc": "  Arm Rest  ",  "code": " 234  "       },{ "price": " 20.10 ",    "qty": "   4  ",  "desc": "  Bench seat  ",  "code": " 1351  "       },{ "price": " 5.10 ",    "qty": "   4  ",  "desc": "  Bucket seat  ",  "code": " 453411  "       },{ "price": " 20.50 ",    "qty": "   5  ",  "desc": "  Children and baby car seat  ",  "code": " 7811  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Fastener  ",  "code": " 13231  "       },{ "price": " 22.10 ",    "qty": "   5  ",  "desc": "  Headrest  ",  "code": " 23411  "       },{ "price": " 120.10 ",    "qty": "   10  ",  "desc": "  Seat belt  ",  "code": " 11  "       },{ "price": " 34.10 ",    "qty": "   22  ",  "desc": "  Seat bracket  ",  "code": " 181  "       },{ "price": " 230.10 ",    "qty": "   30  ",  "desc": "  Seat cover ",  "code": " 711  "       },{ "price": " 23.10 ",    "qty": "   50  ",  "desc": "  Seat track  ",  "code": " 14561  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Other seat components  ",  "code": " 1134  "       },{ "price": " 202.10 ",    "qty": "   10  ",  "desc": "  Back seat  ",  "code": " 11311  "       },{ "price": " 210.10 ",    "qty": "   11  ",  "desc": "  Front seat  ",  "code": " 234234  "       }] """
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
        
        buffer = ''
        buffer += oneRecord['qty'] + ','
        totalQty += float(oneRecord[qty])
        
    print("total qty is" + str (totalQty)) 
    return jsonify(buffer + '' + str (totalQty))


@app.route('/getPrice')
def getprice():

    x = """
    [{"price": " 40.50 ",    "qty": "   1  ",  "desc": "  Arm Rest  ",  "code": " 234  "       },{ "price": " 20.10 ",    "qty": "   4  ",  "desc": "  Bench seat  ",  "code": " 1351  "       },{ "price": " 5.10 ",    "qty": "   4  ",  "desc": "  Bucket seat  ",  "code": " 453411  "       },{ "price": " 20.50 ",    "qty": "   5  ",  "desc": "  Children and baby car seat  ",  "code": " 7811  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Fastener  ",  "code": " 13231  "       },{ "price": " 22.10 ",    "qty": "   5  ",  "desc": "  Headrest  ",  "code": " 23411  "       },{ "price": " 120.10 ",    "qty": "   10  ",  "desc": "  Seat belt  ",  "code": " 11  "       },{ "price": " 34.10 ",    "qty": "   22  ",  "desc": "  Seat bracket  ",  "code": " 181  "       },{ "price": " 230.10 ",    "qty": "   30  ",  "desc": "  Seat cover ",  "code": " 711  "       },{ "price": " 23.10 ",    "qty": "   50  ",  "desc": "  Seat track  ",  "code": " 14561  "       },{ "price": " 20.10 ",    "qty": "   2  ",  "desc": "  Other seat components  ",  "code": " 1134  "       },{ "price": " 202.10 ",    "qty": "   10  ",  "desc": "  Back seat  ",  "code": " 11311  "       },{ "price": " 210.10 ",    "qty": "   11  ",  "desc": "  Front seat  ",  "code": " 234234  " }]"""
    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(type(y))

    ## just for the first list 
    print(y[0])

    totalprice = 0 

    for oneRecord in y:
        print(oneRecord)
        # just select the qty 
        print(oneRecord['price'])
        ## add the qty to the running total 
        
        buffer = ''
        buffer += oneRecord['price'] + ','
        totalprice += float(oneRecord[price])
        
    print("total price is" + str (totalprice)) 
    return jsonify(buffer + '' + str (totalprice))




app.run()