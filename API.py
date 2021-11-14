import requests
res = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060')
print(res.status_code)
print(res.text)