#from pyfiglet import figlet_format

#print(figlet_format("Harsh Tripathi "))


import requests

r = requests.get("https://api.github.com")
print(r.status_code)
print(r.json()["current_user_url"])

# requets module is used to make HTTP requests in Python. It allows you to send HTTP/1.1 requests easily.
# You can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access the response data in the same way.
# It is a popular third-party library that simplifies the process of working with HTTP requests compared to the built-in urllib library.
# To use the requests module, you need to install it first using pip:
# pip install requests  
# After installing, you can import it in your Python script and start making HTTP requests.