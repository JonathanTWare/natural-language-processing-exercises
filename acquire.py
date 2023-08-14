

def get_blog_articles(urls):
    articles_data = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('h1').text.strip()
        content = ' '.join([p.text.strip() for p in soup.find_all('p')])
        
        article = {
            'title': title,
            'content': content
        }
        articles_data.append(article)
    
    return articles_data

urls_to_scrape = [
    "https://codeup.edu/alumni-stories/how-i-paid-43-for-my-codeup-tuition/",
    "https://codeup.edu/featured/women-in-tech-panelist-spotlight/",
    "https://codeup.edu/featured/women-in-tech-rachel-robbins-mayhill/",
    "https://codeup.edu/codeup-news/women-in-tech-panelist-spotlight-sarah-mellor/",
    "https://codeup.edu/events/women-in-tech-madeleine/",
    "https://codeup.edu/codeup-news/panelist-spotlight-4/",
]


articles_data = get_blog_articles(urls_to_scrape)



def scrape_articles(urls):
    articles_data = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        
        title_element = soup.find('span', itemprop='headline')
        if title_element:
            title = title_element.text.strip()
        else:
            title = "Title not found"
        content = soup.find(itemprop="articleBody")
        if content:
            content = content.text.strip()
        else:
            content = "Title not found"
        
        category = url.split('/')[-1]
        
        article = {
            'title': title,
            'content': content,
            'category': category
            
        }
        articles_data.append(article)
    
    return articles_data
'''
ex. usage ...

urls_to_scrape = [
    "https://inshorts.com/en/read/business",
    "https://inshorts.com/en/read/sports",
    "https://inshorts.com/en/read/technology",
    "https://inshorts.com/en/read/entertainment",
]


articles_data = scrape_articles(urls_to_scrape)

'''

def scrape_inshorts_articles(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []

        article_cards = soup.find_all(itemtype='http://schema.org/NewsArticle')

        for card in article_cards:
            headline = card.find('span', itemprop='headline').text
            summary = card.find('div', itemprop='articleBody').text
            category = url.split('/')[-1]
            
            articles.append({
                'headline': headline,
                'summary': summary,
                'category': category,
            })

        
'''
ex. usage... 

if __name__ == "__main__":
    urls = [
        "https://inshorts.com/en/read/business",
        "https://inshorts.com/en/read/sports",
        "https://inshorts.com/en/read/technology",
        "https://inshorts.com/en/read/entertainment"
    ]
    scrape_inshorts_articles(urls)
    
'''

import requests
from bs4 import BeautifulSoup

def scrape_inshorts_articles(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []

        article_cards = soup.find_all(itemtype='http://schema.org/NewsArticle')

        for card in article_cards:
            headline = card.find('span', itemprop='headline').text
            summary = card.find('div', itemprop='articleBody').text

            articles.append({
                'headline': headline,
                'summary': summary
            })

'''
ex. usage...


if __name__ == "__main__":
    base_url = "https://inshorts.com/en/read/"
    pages = [
        "business",
        "sports",
        "technology",
        "entertainment",
        "india",
        "politics",
        "startups",
        "hatke",
        "international",
        "automobile",
        "science",
        "travel",
        "miscellaneous",
        "fashion",
        "education",
        
    ]      

    urls = [base_url + page for page in pages]
    scrape_inshorts_articles(urls)

'''

    

