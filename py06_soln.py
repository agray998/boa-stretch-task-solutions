#! venv/bin/python3
import requests
from time import sleep

if __name__ == '__main__':
    delay = 2
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response() # if the request fails with an exception, just create an empty response object as placeholder
    while response.status_code == None or response.status_code >= 500:
        if delay > 60:
            print("too many failed attempts")
            break
        print("Error: " + response.headers.get("ERROR", "No Error header received"))
        sleep(delay)
        try:
            response = requests.get('http://localhost:5000/api/flaky')
        except:
            response = requests.Response()
        delay *= 2
    else:
        print(response.json())