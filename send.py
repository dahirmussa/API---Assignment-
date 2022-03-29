import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"

    # Example calling the echo method
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(url, json=payload).json()
    print(response)
    # Select just the result item from the JSON
    print(response["result"])
    
    # Call the input function just to hang the console.
    input()

if __name__ == "__main__":
    main()