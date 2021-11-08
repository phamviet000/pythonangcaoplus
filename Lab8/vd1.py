import urllib.request
url_google = urllib.request.urlopen('https://www.google.com/')
#print(url_google.read())
#print(url_google.readline())
#print(url_google.readlines())
#print(url_google.fileno())
#print(url_google.info())
print(url_google.getcode())
print(url_google.geturl())





