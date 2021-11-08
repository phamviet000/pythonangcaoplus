import urllib.parse
import urllib.request
try:
    url = urllib.request.urlopen('https://www.vietdeptrai.org/')
    print(url.read())
except urllib.error.URLError as e:
    print('Error: ',e.reason)







