from six.moves import urllib
import json
import requests
import lxml.etree
import lxml.html
from bs4 import BeautifulSoup
from config import LAST_ACCESS, post_listing


def TRADEGOV_update():
    url = makeParams('electricity')
    results = parse_request(url)['results']
    collect_leads(results)

def collect_leads(lead_data):
    count = 0
    pub_date = ''
    for result in lead_data:
        # print(result)
        print('*************** RESULT # ' + str(count) + " ***************")
        # print('published_at: ', result['publish_date'])
        # print('hosted_url: ', result['url'])
        # print('source: ', result['source'])
        # print('contract_number: ', result['id'])
        # # print('industries: ', result['industries'])
        # print('country: ', result['country_name'])
        # print('description: ', result['description'])
        # print('summary: ', result['description'][:150])
        pub_date = result['publish_date'][0:19] + result['publish_date'][23:]

        # print(pub_date[0:5]+pub_date[7:])
        # try:
        #     print('implementing_entity: ', result['funding_source'])
        #     print('reference_number: ', result['reference_number'])
        #     print('click link: ', result['click_url'])
        # except:
        #     pass
        post_listing(result['trade_region'][0], pub_date, pub_date, result['title'], result['description'], result['description'][:150], 'd4289cd6-563d-4ec6-b1b5-82d49a15ad07')
        count += 1

def makeParams(query):
    API_KEY = 'API KEY HERE'
    request_url = 'https://api.trade.gov/v1/trade_leads/search?api_key=' + API_KEY + '&q=' + query
    return request_url

def parse_request(url):
    r = requests.get(url)
    data_dict = r.json()
    return data_dict


TRADEGOV_update()
