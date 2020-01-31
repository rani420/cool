#%7B = {
#%7D = }
#%22 = "
#%3A = :
#%2C = ,


q_hash = 'e769aa130647d2354c40ea6a439bfc08'
iid = '5856087167'
after = 'QVFDaFNEbWQ1ZWRKeDN2UWtSWmdBejV4NW13Q3RoWnI0aGYxVmdmOHRmQm50S0VjYWRWdUJjcXlvbjFJWWlqQkNKTDNyXzc1VTc3anlQdkRGb19VdnVfdg%3D%3D'
count = 12

api_endpoint = f'https://www.instagram.com/graphql/query/?query_hash={q_hash}&variables=%7B%22id%22%3A%22{iid}%22%2C%22first%22%3A{count}%2C%22after%22%3A%22{after}%22%7D'

import requests as req
from bs4 import BeautifulSoup as bs

r = req.get(api_endpoint)
r_dict = r.json()
type(r_dict)
img = r_dict['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['display_url']
end_cursor = r_dict['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
shortcode = r_dict['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']
print(img)
print(end_cursor)
print(shortcode)
