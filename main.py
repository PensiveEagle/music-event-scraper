import requests
import selectorlib

url = "https://programmer100.pythonanywhere.com/tours/"

def scrape( page_url: str ) -> str:
    """
    Scrape the source HTML from the URL
    """
    
    response = requests.get( page_url )
    source_html = response.text

    return source_html

def extract_data( html_content: str ) -> str:
    """
    Extract the content of element defined in extract.yaml
    """
    
    extractor = selectorlib.Extractor.from_yaml_file( "extract.yaml" )
    value = extractor.extract( html_content )[ "tours" ]
    return value

if __name__ == "__main__":
    scraped_data = scrape( url ) 
    extracted_data = extract_data( scraped_data )
    print( extracted_data )
