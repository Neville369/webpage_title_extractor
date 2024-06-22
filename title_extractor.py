from bs4 import BeautifulSoup as bs 
import requests as rq
import lxml
import re 

# Read URLs from the text file 
with open('urls.txt','r') as file:
    urls = [line.strip().rstrip(',') 
            for line in file 
            if line.strip()]

# A function to get the title of a webpage 
def get_title(url):
    try:
        response = rq.get(url)
        response.raise_for_status()
        soup = bs(response.content,'lxml')
        title = soup.find('title').text
        return title 
    except rq.RequestException as e:
        return 
    
# Iterate over each url and print the title 
for url in urls:
    if url:
        title = get_title(url)
        print (f'Title of {url}:{title}')