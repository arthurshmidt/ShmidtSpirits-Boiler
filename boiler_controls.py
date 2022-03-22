import requests
import time
# import relay_class

API_URL = "http://192.168.1.157:5000/boiler"

def main():
    while(True):
        response = requests.get(API_URL)
        print(response.json())
        print("test")
        time.sleep(5)

if __name__ == '__main__':
    main()
