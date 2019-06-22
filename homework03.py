import requests

url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808' 
response = requests.get(url)
HTML=response.text
URLS=HTML.split('\n')
lines=HTML.split('\n')

for url in URLS:
    response = requests.get(url)
    content = response.content
    # print(content)
    name= url.split('/')[-1]

    # print(name)
    with open(name,'wb') as f:
        f.write(content)