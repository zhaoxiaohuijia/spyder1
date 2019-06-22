import urllib.request
url ='https://www.17k.com/chapter/2933095/36699279.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
html=response.read().decode('utf8')
print(html)







import urllib.request
urls = 'https://www.jianshu.com/'
import random
seq=[{'http':'http://222.182.53.200:8118'},{'http':'http://2223.241.116.36:8010'}]
t=random.choice(seq)
print(t)
for t in seq:
	proxy = urllib.request.ProxyHandler(seq)
	opener = urllib.request.build_opener(proxy)
	response = opener.open(urls)
	if(reponse.status==200):
    		print(reponse.status)
		print("成功")
	else:
		print("失败")