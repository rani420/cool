#%7B = {
#%7D = }
#%22 = "
#%3A = :
#%2C = ,
# v1 = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][0]['node']['video_url']


c =6

q_hash = 'e769aa130647d2354c40ea6a439bfc08'
iid = '5856087167'
after = ''
count = 50

api_endpoint = f'https://www.instagram.com/graphql/query/?query_hash={q_hash}&variables=%7B%22id%22%3A%22{iid}%22%2C%22first%22%3A{count}%2C%22after%22%3A%22{after}%22%7D'

import requests as req
from bs4 import BeautifulSoup as bs

r = req.get(api_endpoint)
r_dict = r.json()
type(r_dict)

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
desc =j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
print(desc)
# v1 = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][4]['node']['video_url']
le = len(j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'])
for h in range(le):
    v = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][h]['node']['video_url']
    print(v)
    print('\n')
