import http.client

conn = http.client.HTTPConnection("localhost", 8000)  

conn.request("GET", "/") 

response = conn.getresponse()

data = response.read()
print(data.decode("utf-8"))

conn.close()


# import http.client

# conn = http.client.HTTPSConnection("github.com")

# conn.request("GET", "/Sudeep72/tour")


# response = conn.getresponse()

# data = response.read()
# print(data.decode("utf-8"))

# conn.close()
