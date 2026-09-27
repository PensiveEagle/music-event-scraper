import requests
import selectorlib

url = "https://programmer100.pythonanywhere.com/tours/"

def scrape(page_url):
    """
    Scrape the source HTML from the URL
    """
    
    response = requests.get( page_url )
    source_html = response.text

    return source_html

if __name__ == "__main__":
    print( scrape( url ) )
