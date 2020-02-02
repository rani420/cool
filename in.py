#%7B = {
#%7D = }
#%22 = "
#%3A = :
#%2C = ,
# v1 = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][0]['node']['video_url']



q_hash = 'e769aa130647d2354c40ea6a439bfc08'
insta_id = '5856087167'
after = ''
count = 50

api_endpoint = f'https://www.instagram.com/graphql/query/?query_hash={q_hash}&variables=%7B%22id%22%3A%22{insta_id}%22%2C%22first%22%3A{count}%2C%22after%22%3A%22{after}%22%7D'

import requests as req
from bs4 import BeautifulSoup as bs

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36"
r = req.get(api_endpoint, headers=headers)
r_dict = r.json()
type(r_dict)

for c in range(count):
    img = r_dict['data']['user']['edge_owner_to_timeline_media']['edges'][c]['node']['display_url']
    end_cursor = r_dict['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    shortcode = r_dict['data']['user']['edge_owner_to_timeline_media']['edges'][c]['node']['shortcode']
    print(img)
    print(end_cursor)
    print(shortcode)
    u = f'https://instagram.com/p/{shortcode}'
    r1 = req.get(u).content
    s1 = bs(r1, 'html.parser')
    print(s1.title.text)
    m = s1.find_all('script')[3].text[21:-1]
    import json
    j = json.loads(m)
    d = json.dumps(j, indent=4)
    try:
        desc =j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
        print(desc)
    except IndexError:
        print("index error")
    # v1 = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][4]['node']['video_url']
    try:
        le = len(j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'])
    except KeyError:
        print('key error')
    for h in range(le):
        try:
            v = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][h]['node']['video_url']
            print(v)
            print('\n')
        except KeyError:
            print('it is photo')
