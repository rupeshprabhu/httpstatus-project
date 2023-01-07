import urllib3
import requests

print("Hello")

http = urllib3.PoolManager()
response = http.request("GET", "https://httpstat.us/403")
print(response.status) # Prints 200 

# r = requests.get('http://goo.gl/NZek5', allow_redirects=False)
r = requests.get('https://httpstat.us/301', allow_redirects=False)
print (r.status_code) 