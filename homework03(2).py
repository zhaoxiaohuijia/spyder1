import requests

url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808' 
response = requests.get(url)
HTML=response.text
URLS=HTML.split('\n')
lines=HTML.split('\n')

for line in lines:
    if '<a href' in lines:
        split_=line.split('http://')
        for i in line:
            if 'http' in i:
                url=i.split('','')[1]
                if 'jpg' in url:
                    URLS.append(url)
for url in URLS:
    response = requests.get(url)
    content1=response.content
    name= url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content1)