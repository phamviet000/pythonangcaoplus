import urllib.request
import json
url_google = urllib.request.urlopen('https://www.google.com/search?q=test')
print(url_google.read())
# khi chạy file bị lỗi urllib.error.HTTPError: HTTP Error 403: Forbidden

