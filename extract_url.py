"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
from urllib.parse import urlparse

def get_domain_name():
    url = input("Enter a valid URL (i.e. https://www.google.com) : ")
    parsed_url = urlparse(url)
    if parsed_url.netloc:
        domain = parsed_url.netloc.split('.')[-2] if parsed_url.netloc.startswith('www.') else parsed_url.netloc.split('.')[-2]
        return domain
    else:
        print("Invalid URL. Please make sure to enter a valid URL.")
        return None

# Example usage
domain_name = get_domain_name()
if domain_name:
    print("Domain name:", domain_name)
