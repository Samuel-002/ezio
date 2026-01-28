from urllib.parse import urlparse

def in_scope(domain, url):
    return urlparse(url).netloc.endswith(domain)
