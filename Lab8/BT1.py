import urllib.request
import json
url_google = urllib.request.urlopen('https://www.google.com/')
content = url_google.read()
print(url_google.read())
f=open('D:\pythonnangcao\gitpy\pythonangcaoplus\Lab8\json1.txt','ab',encoding='utf-8')
f.write(content)
f.close()




