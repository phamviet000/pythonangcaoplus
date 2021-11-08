import urllib.request
url_google = urllib.request.urlopen('https://www.python.org/search/?q=urlopen')
print(url_google.read())






