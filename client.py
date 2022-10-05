import requests

url = 'http://localhost:8080/'
obj = {"Test": "Test"}

requests.post(url, data = obj)