import requests
url_link = input("enter a url link: " )
r = requests.get(url_link)
if r.status_code == 200:
    print("true")
else:
    print("false")    
