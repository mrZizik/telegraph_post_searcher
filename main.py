import socket
from multiprocessing import Pool

URL = "telegra.ph"
THEADS = 16

def checkurl(query):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((URL, 80))
        s.send("GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(query, URL).encode('utf-8'))
        return s.recv(12).endswith("200".encode('utf-8'))

def generate_urls(title, months):
    for i in months:
        for j in range(1,32):
            yield title + "-" + str(i).zfill(2) + "-" + str(j).zfill(2)

def step(query):
    temp = 1
    tempquery = query
    found = []
    while checkurl(tempquery):
        found.append("http://{}/{} exists".format(URL,tempquery))
        temp += 1
        tempquery = query + "-" + str(temp)
    return "\n".join(found)

title = input("Search title: ").lower()
months = input("Months to search within divided by comma (11,12,1): ").split(",")

with Pool(THEADS) as p:
    print("\n".join(list(filter(None, p.map(step, generate_urls(title, months))))))




