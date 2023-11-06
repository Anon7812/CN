import http.client

conn = http.client.HTTPConnection("localhost", 8000)

for _ in range(3):
    conn.request("GET", "/")  
    response = conn.getresponse()
    data = response.read()
    print(data.decode("utf-8"))

conn.close()
