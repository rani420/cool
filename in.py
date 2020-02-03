#%7B = {
#%7D = }
#%22 = "
#%3A = :
#%2C = ,
# v1 = j['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][0]['node']['video_url']



q_hash = 'e769aa130647d2354c40ea6a439bfc08'
insta_id = '5856087167'
after = ''
count = 12

api_endpoint = f'https://www.instagram.com/graphql/query/?query_hash={q_hash}&variables=%7B%22id%22%3A%22{insta_id}%22%2C%22first%22%3A{count}%2C%22after%22%3A%22{after}%22%7D'

import requests as req
from bs4 import BeautifulSoup as bs
import json

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36"
r = req.get(api_endpoint, headers=headers)
r_json = r.json()
end_cursor = r_json['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']

for c in range(count):
    print(c+1)
    print('\n')
    print('\n')
    shortcode = r_json['data']['user']['edge_owner_to_timeline_media']['edges'][c]['node']['shortcode']
    img = r_json['data']['user']['edge_owner_to_timeline_media']['edges'][c]['node']['display_url']
    print(shortcode)
    print('\n')
    print('\n')
    short_code_url = f'https://instagram.com/p/{shortcode}'
    short_code_r = req.get(short_code_url).content
    short_code_s = bs(short_code_r, 'html.parser')
#     print(short_code_s.title.text)
    script_tag_text = short_code_s.find_all('script')[3].text[21:-1]
    json_data = json.loads(script_tag_text)
    json_indent = json.dumps(json_data, indent=4)
    try:
        imgs = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
        for img in imgs:
            t = img['node']['display_url']
            print(t)
            print('\n')
    except Exception as e:
        imgs = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']
        print(imgs)
        print('\n')
        print(e)

    try:
        desc =json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
        print(desc)
        print('\n')
    except Exception as e:
        print(e)
    try:
        posts = len(json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'])
        for post in range(posts):
            try:
                video_url = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][post]['node']['video_url']
                print(video_url)
                print('\n')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    print('\n')
    print('\n')
