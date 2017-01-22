import urllib



def checkfound(query):
    response = urllib.urlopen("http://telegra.ph/"+query)
    return response.getcode()==200

title = raw_input("Search title: ").lower()
months = raw_input("Months to search within divided by comma (11,12,1): ").split(",")
for i in months:
    for j in xrange(1,32):
        num = 1
        int_query = title + "-" + str(i).zfill(2) + "-" + str(j).zfill(2)
        query = int_query
        while checkfound(query):
            print "http://telegra.ph/"+query, " found"
            num+=1
            query = int_query+"-"+str(num)




