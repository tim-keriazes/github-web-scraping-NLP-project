from requests import get
from bs4 import BeautifulSoup
import os
import re
import json
from env import github_token, github_username
import pandas as pd
import requests
import time

def create_urls(num=1759):
    ''' this function scrapes the cryptography repositories from github and returns a list of urls
    '''
    num_of_repos=num

    page_numbers = [i for i in range(0,101)]
    print(page_numbers)
    urls = [f'https://github.com/search?p={i}&q=%23defi&type=Repositories' for i in page_numbers]

    print(urls)
    return urls

def get_endpoints(url):
    ''' This function gets the endpoints from the list of above urls
    '''

    headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}
    
    while True:
        response = requests.get(url, headers=headers)
        if response.ok:
            break
        else:
            print('sleeping')
            time.sleep(20)
            continue
    soup = BeautifulSoup(response.text)
    
    print(response.ok)

    endpoints = []
    subgroups = soup.find_all('div', {"class":"f4 text-normal"})

    for group in subgroups:
        endpoints.append(re.search('href=".*"', str(group))[0][6:-1])

    return endpoints

def make_all_endpoints():
    ''' This function returns all of the endpoints
    '''
    urls = create_urls()
    for url in urls:
        print(url)
    all_endpoints = []

    for i, page in enumerate(urls):
        all_endpoints.append(get_endpoints(page))
        print(page)

    print(len(all_endpoints))

    return all_endpoints

def acquire_endpoints():
    ''' This function acquires all endpoints and writes them to a csv.
    '''
    our_endpoints = pd.Series(make_all_endpoints())
    our_endpoints.to_csv('endpoints.csv', index=False)

    return our_endpoints

def flatten_endpoints():
    ''' This function flattens a 2d array into a 1d array
    '''
    end_points = pd.read_csv('endpoints.csv')
    all_values = []
    for value in end_points.values:
        for ep in value:
            all_values.append(ep)

    final_values = []
    #print(all_values)
    for value in all_values:
        for val in value.split("'"):
            if len(val) > 3:
                final_values.append(val)
                print(val)

    return pd.Series(final_values, name='endpoints')



def get_article(url):
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.select('.entry-title')[0].text
    content = soup.select('.entry-content')[0].text
    output = {
        'title':title.strip(),
        'content':content.strip()
    }
    return output

def get_blog_articles(url_list):
    output = []
    for url in url_list:
        article_dict = get_article(url)
        output.append(article_dict)
    return output

def get_articles(url, category):
    headers = {'User-Agent': 'Codeup Data Science'}
    outputs = []
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_cards = soup.select('.news-card')
    for card in news_cards:
        title = card.select('.news-card-title')[0].text
        title = re.findall('(\s.*)', title)[1]
        content = card.select('.news-card-content')[0].text
        output = {
            'title':title.strip(),
            'content':content.strip(),
            'category':category
        }
        outputs.append(output)
    return outputs

def get_links(url):
    links = []
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.select('h2 a[href]'):
        links.append(link['href'])
    return links

def get_news_articles():
    outputs = []
    base_url = 'https://inshorts.com/en/read'
    end_points = ['business', 'sports', 'technology', 'entertainment'] 
    for endp in end_points:
        outputs += get_articles(f"{base_url}/{endp}", endp)
    return outputs

def cache_data(dictionary, filename='cache_file.json'):
    json_obj = json.dumps(dictionary, indent = 4)
    try:
        with open(filename, 'w') as f:
            f.write(json_obj)
        return True
    except Exception as e:
        print(e)
        return False
    
def read_url_or_file_inshort(filename='inshort_articles.json', query_url=False):
    if os.path.isfile(filename) and not query_url:
        print('Found File')
        try:
            with open(filename, 'r') as f:
                json_obj = json.load(f)
            return json_obj
        except Exception as e:
            print(e)
            return None
    else:
        print('Querying url')
        try:
            dictionary = get_news_articles()
            cache_data(dictionary, filename=filename)
            return dictionary
        except Exception as e:
            print(e)
            return None
            
def read_url_or_file_codeup(filename='codeup_articles.json', query_url=False):
    if os.path.isfile(filename) and not query_url:
        print('Found File')
        try:
            with open(filename, 'r') as f:
                json_obj = json.load(f)
            return json_obj
        except Exception as e:
            print(e)
            return None
    else:
        print('Querying url')
        url_home = 'https://codeup.com/blog/'
        select_articles = get_links(url_home)
        try:
            dictionary = get_blog_articles(select_articles)
            cache_data(dictionary, filename=filename)
            return dictionary
        except Exception as e:
            print(e)
            return None

def read_url_or_file_repo(filename='data.json', query_url=False):
    if os.path.isfile(filename) and not query_url:
        print('Found File')
        try:
            with open(filename, 'r') as f:
                json_obj = json.load(f)
            return json_obj
        except Exception as e:
            print(e)
            return None
    else:
        print('Querying url')
        url_home = 'https://codeup.com/blog/'
        select_articles = get_links(url_home)
        try:
            dictionary = get_blog_articles(select_articles)
            cache_data(dictionary, filename=filename)
            return dictionary
        except Exception as e:
            print(e)
            return None