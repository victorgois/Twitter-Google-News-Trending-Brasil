from newsapi import NewsApiClient
import time
from datetime import datetime,timedelta, date
import json

timestr = time.strftime("%Y%m%d-%H")

# Init
newsapi = NewsApiClient(api_key='2de5d157d448424db4574be570b492d4')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(language='pt',
#                                          country='br',
#                                          )

everything = newsapi.get_everything(
    q='Paulo Guedes',
    from_param='2020-07-08',
    to='2020-07-10',
    sort_by= 'relevancy')

""" with open('./google-news/googlenews' + timestr + '.json','w') as f:
    json.dump(top_headlines,f,indent=4) """

with open('./google-news/guedes' + '.json','w') as f:
    json.dump(everything,f,indent=4)

