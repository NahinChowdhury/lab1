import requests

print(requests.__version__)

print(requests.get("https://www.google.com/teapot").text)

print(requests.get("https://raw.githubusercontent.com/NahinChowdhury/lab1/master/script.py").text)