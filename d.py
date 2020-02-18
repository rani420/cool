
import requests as req
from bs4 import BeautifulSoup as bs
for re in range(1,201):
    if re ==1:
        url = 'http://masalaseen.com'
    else:
        url = f'http://masalaseen.com/page/{re}'
    print(re)
    r1 = req.get(url).content
    s1 = bs(r1, 'html.parser')
    a = s1.find_all('a', title=True, rel=False)
    a.pop()
    a.pop()
    ah = []
    for i in a:
        ah.append(i['href'])
    vs = []
    for j in ah:
        r2 = req.get(j).content
        s2 = bs(r2, 'html.parser')
        vid = s2.find('source')['src']
        img = s2.find_all('img')[2]['src']
        payload = {
            'num1':img,
            'num2':vid
        }
        r3 = req.get('https://for.pythonanywhere.com/upload', params=payload)
        print(r3.content)
